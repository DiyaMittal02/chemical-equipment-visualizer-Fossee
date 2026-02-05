from django.contrib import admin
from .models import EquipmentDataset, EquipmentRecord


@admin.register(EquipmentDataset)
class EquipmentDatasetAdmin(admin.ModelAdmin):
    list_display = ['filename', 'uploaded_by', 'uploaded_at', 'total_count']
    list_filter = ['uploaded_at', 'uploaded_by']
    search_fields = ['filename']
    readonly_fields = ['uploaded_at']


@admin.register(EquipmentRecord)
class EquipmentRecordAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']
    list_filter = ['equipment_type', 'dataset']
    search_fields = ['equipment_name', 'equipment_type']
