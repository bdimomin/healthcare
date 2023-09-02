from django.contrib import admin
from appointment.models import Appointment



# class AppoinmentAdmin(admin.ModelAdmin):
#     list_display = ('appoinment_date','patient_name','department_name', 'doctor_name')
#     search_fields=('appoinment_date', 'department_name','doctor_name')
#     filter_horizontal=()
#     fieldsets=()
#     list_filter=('department_name',)

#     add_fieldsets = (
#             (None, {
#                 'classes': ('wide'),
#                 'fields': ('appoinment_date','patient_name','department_name', 'doctor_name'),
#             }),
#         )
    
#     ordering = ['appoinment_date']


# admin.site.register(Appointment,AppoinmentAdmin)  
