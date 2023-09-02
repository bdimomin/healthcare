from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Patient

class PatientAdmin(BaseUserAdmin):
    list_display = ('name','email', 'phone','is_admin')
    search_fields=('email', 'phone')
    filter_horizontal=()
    fieldsets=()
    list_filter=('last_login',)

    add_fieldsets = (
            (None, {
                'classes': ('wide'),
                'fields': ('name', 'email', 'phone', 'password1','password2'),
            }),
        )
    
    ordering = ['name']

admin.site.register(Patient,PatientAdmin)
