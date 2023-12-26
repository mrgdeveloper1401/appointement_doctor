from django.contrib import admin
from .models import appointmentDate, Patient


class AppointmentDateInline(admin.TabularInline):
    model = appointmentDate
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = (AppointmentDateInline,)
    list_display = ('get_full_name', 'nation_code', 'email', 'insurance_number')
    list_per_page = 30
    list_filter = ('create_at', 'update_at')
    search_fields = ('get_full_name', 'nation_code', 'email', 'insurance_number')
    readonly_fields = ('create_at', 'update_at')


@admin.register(appointmentDate)
class AppointmentDateAdmin(admin.ModelAdmin):
    pass