from django.db import models
from django.contrib.auth.models import User
import json


class EquipmentDataset(models.Model):
    """Model to store uploaded equipment datasets"""
    
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255)
    total_count = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    equipment_distribution = models.TextField()  # JSON string
    csv_data = models.TextField()  # Store CSV content
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.filename} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
    def get_distribution_dict(self):
        """Get equipment distribution as dictionary"""
        return json.loads(self.equipment_distribution)
    
    def set_distribution_dict(self, dist_dict):
        """Set equipment distribution from dictionary"""
        self.equipment_distribution = json.dumps(dist_dict)


class EquipmentRecord(models.Model):
    """Individual equipment record"""
    
    dataset = models.ForeignKey(EquipmentDataset, on_delete=models.CASCADE, related_name='records')
    equipment_name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=100)
    flowrate = models.FloatField()
    pressure = models.FloatField()
    temperature = models.FloatField()
    
    def __str__(self):
        return f"{self.equipment_name} ({self.equipment_type})"
