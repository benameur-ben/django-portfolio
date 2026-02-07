"""
Django REST Framework serializers for API endpoints.
"""

from rest_framework import serializers
from .models import Project, Service, LeadCapture


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'tech_stack', 
            'github_link', 'demo_link', 'role', 'featured', 
            'image', 'created_date'
        ]
        read_only_fields = ['id', 'created_date']


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for Service model."""
    
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = Service
        fields = ['id', 'name', 'category', 'category_display', 'description', 'icon', 'order']
        read_only_fields = ['id']


class LeadCaptureSerializer(serializers.ModelSerializer):
    """Serializer for LeadCapture model with validation."""
    
    class Meta:
        model = LeadCapture
        fields = ['id', 'name', 'email', 'company', 'message', 'service_interest', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_email(self, value):
        """Ensure email is lowercase and trimmed."""
        return value.lower().strip()
