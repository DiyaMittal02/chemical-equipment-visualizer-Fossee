from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EquipmentDataset, EquipmentRecord


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class EquipmentRecordSerializer(serializers.ModelSerializer):
    """Serializer for individual equipment records"""
    
    class Meta:
        model = EquipmentRecord
        fields = ['id', 'equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']


class EquipmentDatasetSerializer(serializers.ModelSerializer):
    """Serializer for equipment datasets"""
    
    uploaded_by = UserSerializer(read_only=True)
    records = EquipmentRecordSerializer(many=True, read_only=True)
    equipment_distribution = serializers.SerializerMethodField()
    
    class Meta:
        model = EquipmentDataset
        fields = [
            'id', 'uploaded_by', 'uploaded_at', 'filename', 
            'total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature',
            'equipment_distribution', 'records'
        ]
    
    def get_equipment_distribution(self, obj):
        """Convert JSON string to dictionary"""
        return obj.get_distribution_dict()


class EquipmentDatasetSummarySerializer(serializers.ModelSerializer):
    """Lightweight serializer for dataset summaries (without full records)"""
    
    uploaded_by = UserSerializer(read_only=True)
    equipment_distribution = serializers.SerializerMethodField()
    
    class Meta:
        model = EquipmentDataset
        fields = [
            'id', 'uploaded_by', 'uploaded_at', 'filename', 
            'total_count', 'avg_flowrate', 'avg_pressure', 'avg_temperature',
            'equipment_distribution'
        ]
    
    def get_equipment_distribution(self, obj):
        """Convert JSON string to dictionary"""
        return obj.get_distribution_dict()
