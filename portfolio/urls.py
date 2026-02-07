"""
URL configuration for portfolio app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API Router
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'leads', views.LeadCaptureViewSet, basename='lead')

app_name = 'portfolio'

urlpatterns = [
    path('api/', include(router.urls)),
]
