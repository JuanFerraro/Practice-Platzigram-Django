""" User admin classes """

# Django
from django.contrib import admin

# Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin."""

    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number', 'website', 'picture')
    
    search_fields = ('user__username','user__email', 'user__first_name', 'user__last_name')
    
    list_filter = ('modified', 'created',
                   'user__is_active',
                   'user__is_staff'
                   )