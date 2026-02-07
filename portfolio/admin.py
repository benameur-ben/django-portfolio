"""
Custom Django admin interface for portfolio management.
Optimized for managing business leads and content.
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Service, LeadCapture


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Projects."""
    
    list_display = ['title', 'role', 'featured', 'created_date', 'tech_stack_display']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description', 'role']
    list_editable = ['featured']
    date_hierarchy = 'created_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'role', 'image')
        }),
        ('Technical Details', {
            'fields': ('tech_stack', 'github_link', 'demo_link')
        }),
        ('Display Options', {
            'fields': ('featured',)
        }),
    )
    
    def tech_stack_display(self, obj):
        """Display tech stack as comma-separated list."""
        if obj.tech_stack:
            return ', '.join(obj.tech_stack[:3]) + ('...' if len(obj.tech_stack) > 3 else '')
        return '-'
    tech_stack_display.short_description = 'Technologies'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for Services."""
    
    list_display = ['name', 'category', 'icon', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'category', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(LeadCapture)
class LeadCaptureAdmin(admin.ModelAdmin):
    """Admin interface for Lead Management with enhanced features."""
    
    list_display = [
        'name', 'email_link', 'company', 'service_interest_display', 
        'created_at', 'contacted_status'
    ]
    list_filter = ['contacted', 'service_interest', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company')
        }),
        ('Lead Details', {
            'fields': ('service_interest', 'message', 'created_at')
        }),
        ('Follow-up', {
            'fields': ('contacted', 'notes'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_contacted', 'mark_as_not_contacted']
    
    def email_link(self, obj):
        """Make email clickable."""
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'
    
    def service_interest_display(self, obj):
        """Display service interest with color coding."""
        if not obj.service_interest:
            return '-'
        
        colors = {
            'automation': '#4CAF50',
            'trading': '#2196F3',
            'web': '#FF9800',
        }
        color = colors.get(obj.service_interest, '#666')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_service_interest_display()
        )
    service_interest_display.short_description = 'Interest'
    
    def contacted_status(self, obj):
        """Display contacted status with visual indicator."""
        if obj.contacted:
            return format_html('<span style="color: green;">✓ Contacted</span>')
        return format_html('<span style="color: orange;">⏳ Pending</span>')
    contacted_status.short_description = 'Status'
    
    @admin.action(description='Mark selected leads as contacted')
    def mark_as_contacted(self, request, queryset):
        """Bulk action to mark leads as contacted."""
        updated = queryset.update(contacted=True)
        self.message_user(request, f'{updated} lead(s) marked as contacted.')
    
    @admin.action(description='Mark selected leads as not contacted')
    def mark_as_not_contacted(self, request, queryset):
        """Bulk action to mark leads as not contacted."""
        updated = queryset.update(contacted=False)
        self.message_user(request, f'{updated} lead(s) marked as not contacted.')


# Customize admin site header
admin.site.site_header = 'Portfolio Administration'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Welcome to Portfolio Management'
