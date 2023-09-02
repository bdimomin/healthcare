from django.contrib import admin
# from doctor.models import Doctor, Departments
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class DoctorAdmin(BaseUserAdmin):
#     list_display = ('bmdc_registration_number','name','email', 'phone','department')
#     search_fields=('email', 'phone','bmdc_registration_number')
#     filter_horizontal=()
#     fieldsets=()
#     list_filter=('last_login',)

#     add_fieldsets = (
#             (None, {
#                 'classes': ('wide'),
#                 'fields': ('bmdc_registration_number','name', 'email','fees','about','phone','doc_image', 'department','password1','password2'),
#             }),
#         )
    
#     ordering = ['bmdc_registration_number']

# admin.site.register(Doctor,DoctorAdmin)

# admin.site.register(Departments)
