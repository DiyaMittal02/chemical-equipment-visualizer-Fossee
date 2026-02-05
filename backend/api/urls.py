from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'datasets', views.EquipmentDatasetViewSet, basename='dataset')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.upload_csv, name='upload-csv'),
    path('summary/<int:dataset_id>/', views.get_summary, name='get-summary'),
    path('history/', views.get_history, name='get-history'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/logout/', views.logout_user, name='logout'),
    path('auth/user/', views.current_user, name='current-user'),
]
