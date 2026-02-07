"""
Database models for the portfolio application.
Optimized with strategic indexing for fast queries.
"""

from django.db import models
from django.core.validators import EmailValidator, URLValidator
from django.utils import timezone


class Project(models.Model):
    """Portfolio projects with tech stack and links."""
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField(default=list, help_text="List of technologies used")
    github_link = models.URLField(validators=[URLValidator()], blank=True)
    demo_link = models.URLField(validators=[URLValidator()], blank=True)
    role = models.CharField(max_length=100, help_text="Your role in the project")
    featured = models.BooleanField(default=False, db_index=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, db_index=True)
    
    class Meta:
        ordering = ['-featured', '-created_date']
        indexes = [
            models.Index(fields=['-featured', '-created_date']),
        ]
    
    def __str__(self):
        return self.title


class Service(models.Model):
    """Services offered (Automation, Trading, Web Development)."""
    
    CATEGORY_CHOICES = [
        ('automation', 'Automation'),
        ('trading', 'Trading'),
        ('web', 'Web Development'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Icon class or emoji")
    is_active = models.BooleanField(default=True, db_index=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'name']
        indexes = [
            models.Index(fields=['category', 'is_active']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class LeadCapture(models.Model):
    """Capture potential client leads."""
    
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    service_interest = models.CharField(
        max_length=20,
        choices=Service.CATEGORY_CHOICES,
        blank=True,
        help_text="Service they're interested in"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    contacted = models.BooleanField(default=False, db_index=True)
    notes = models.TextField(blank=True, help_text="Internal notes")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        indexes = [
            models.Index(fields=['contacted', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.email}"


# Custom manager for common queries
class ProjectManager(models.Manager):
    def featured(self):
        return self.filter(featured=True)
    
    def by_tech(self, tech):
        return self.filter(tech_stack__contains=[tech])


# Add custom manager to Project
Project.add_to_class('objects', ProjectManager())
