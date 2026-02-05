from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
import io
from .models import EquipmentDataset, EquipmentRecord
from .serializers import (
    EquipmentDatasetSerializer, 
    EquipmentDatasetSummarySerializer,
    UserSerializer
)
from .utils import generate_pdf_report


class EquipmentDatasetViewSet(viewsets.ModelViewSet):
    """ViewSet for managing equipment datasets"""
    
    queryset = EquipmentDataset.objects.all()
    serializer_class = EquipmentDatasetSerializer
    permission_classes = [AllowAny]  # Changed for easier testing
    
    def get_serializer_class(self):
        """Use summary serializer for list view"""
        if self.action == 'list':
            return EquipmentDatasetSummarySerializer
        return EquipmentDatasetSerializer
    
    @action(detail=True, methods=['get'])
    def download_pdf(self, request, pk=None):
        """Generate and download PDF report for a dataset"""
        dataset = self.get_object()
        pdf_buffer = generate_pdf_report(dataset)
        
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{dataset.filename}_report.pdf"'
        return response


@api_view(['POST'])
def upload_csv(request):
    """Handle CSV file upload and processing"""
    
    if 'file' not in request.FILES:
        return Response(
            {'error': 'No file provided'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    csv_file = request.FILES['file']
    
    # Validate file extension
    if not csv_file.name.endswith('.csv'):
        return Response(
            {'error': 'File must be a CSV'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        # Validate required columns
        required_columns = ['Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return Response(
                {'error': f'Missing required columns: {", ".join(missing_columns)}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Calculate statistics
        total_count = len(df)
        avg_flowrate = df['Flowrate'].mean()
        avg_pressure = df['Pressure'].mean()
        avg_temperature = df['Temperature'].mean()
        
        # Get equipment type distribution
        equipment_distribution = df['Type'].value_counts().to_dict()
        
        # Store CSV content as string
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_content = csv_buffer.getvalue()
        
        # Create dataset
        dataset = EquipmentDataset.objects.create(
            uploaded_by=request.user if request.user.is_authenticated else None,
            filename=csv_file.name,
            total_count=total_count,
            avg_flowrate=avg_flowrate,
            avg_pressure=avg_pressure,
            avg_temperature=avg_temperature,
            csv_data=csv_content
        )
        dataset.set_distribution_dict(equipment_distribution)
        dataset.save()
        
        # Create individual records
        for _, row in df.iterrows():
            EquipmentRecord.objects.create(
                dataset=dataset,
                equipment_name=row['Equipment Name'],
                equipment_type=row['Type'],
                flowrate=row['Flowrate'],
                pressure=row['Pressure'],
                temperature=row['Temperature']
            )
        
        # Maintain history limit
        maintain_dataset_history()
        
        # Return created dataset
        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response(
            {'error': f'Error processing CSV: {str(e)}'}, 
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_summary(request, dataset_id):
    """Get summary statistics for a specific dataset"""
    
    try:
        dataset = EquipmentDataset.objects.get(id=dataset_id)
        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data)
    except EquipmentDataset.DoesNotExist:
        return Response(
            {'error': 'Dataset not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['GET'])
def get_history(request):
    """Get list of last 5 uploaded datasets"""
    
    datasets = EquipmentDataset.objects.all()[:settings.MAX_DATASET_HISTORY]
    serializer = EquipmentDatasetSummarySerializer(datasets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    """Register a new user"""
    
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    
    if not username or not password:
        return Response(
            {'error': 'Username and password are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(username=username, password=password, email=email)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    """Login user"""
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Username and password are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response(
            {'error': 'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(['POST'])
def logout_user(request):
    """Logout user"""
    
    logout(request)
    return Response({'message': 'Logged out successfully'})


@api_view(['GET'])
def current_user(request):
    """Get current authenticated user"""
    
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


def maintain_dataset_history():
    """Keep only the last MAX_DATASET_HISTORY datasets"""
    
    datasets = EquipmentDataset.objects.all()
    if datasets.count() > settings.MAX_DATASET_HISTORY:
        # Delete oldest datasets beyond the limit
        to_delete = datasets[settings.MAX_DATASET_HISTORY:]
        for dataset in to_delete:
            dataset.delete()
