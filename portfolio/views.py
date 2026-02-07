"""
Views for portfolio application.
Includes both template views and RESTful API endpoints.
"""

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from .models import Project, Service, LeadCapture
from .serializers import ProjectSerializer, ServiceSerializer, LeadCaptureSerializer


# Template Views
def index(request):
    """Main portfolio page."""
    context = {
        'featured_projects': Project.objects.featured()[:6],
        'services': Service.objects.filter(is_active=True),
    }
    return render(request, 'index.html', context)


# API ViewSets
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for projects.
    Supports filtering by tech_stack and featured status.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        queryset = Project.objects.all()
        
        # Filter by featured status
        featured = self.request.query_params.get('featured')
        if featured is not None:
            queryset = queryset.filter(featured=featured.lower() == 'true')
        
        # Filter by tech stack
        tech = self.request.query_params.get('tech')
        if tech:
            queryset = queryset.filter(tech_stack__contains=[tech])
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get only featured projects."""
        featured_projects = Project.objects.featured()
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for services.
    Only returns active services.
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get services grouped by category."""
        categories = {}
        for service in self.get_queryset():
            category = service.get_category_display()
            if category not in categories:
                categories[category] = []
            categories[category].append(ServiceSerializer(service).data)
        return Response(categories)


class LeadCaptureThrottle(AnonRateThrottle):
    """Custom throttle for lead capture - 5 submissions per hour."""
    rate = '5/hour'


class LeadCaptureViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lead capture.
    POST only - create new leads.
    """
    queryset = LeadCapture.objects.all()
    serializer_class = LeadCaptureSerializer
    http_method_names = ['post']  # Only allow POST
    throttle_classes = [LeadCaptureThrottle]
    
    def create(self, request, *args, **kwargs):
        """Create a new lead with custom response."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {
                'message': 'Thank you for your interest! I will get back to you soon.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
