from django.contrib import admin
from .models import Clinic, ContactClinic, ClinicType, License


class LicenseInline(admin.TabularInline):
    model = License
    extra = 0


class ClinicTypeInline(admin.TabularInline):
    model = ClinicType
    extra = 0


class ContactClinicInline(admin.TabularInline):
    model = ContactClinic
    extra = 0


@admin.register(Clinic)
class clinic(admin.ModelAdmin):
    inlines = (ClinicTypeInline, ContactClinicInline, LicenseInline)
    list_display = ('clinic_name', 'clinic_address', 'clinic_postal_code','start_date', 'establishment_date', 'doctor_count')
    search_fields = ('clinic_name',)
    list_filter = ('is_active_clinic', 'start_date', 'end_date', 'establishment_date', 'create_at', 'update_at')
    ordering = ('clinic_name', )
    list_per_page = 20

@admin.register(ContactClinic)
class ContactClinicAdmin(admin.ModelAdmin):
    list_display = ('landing_phone','mobile_phone', 'email', 'is_active', 'description')
    search_fields = ('landing_phone','mobile_phone', 'email')
    list_filter = ('is_active', 'create_at', 'update_at')
    ordering = ('landing_phone',)
    list_per_page = 20


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_filter = ('create_at', 'update_at')