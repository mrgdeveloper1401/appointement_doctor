from django.contrib import admin
from .models import City, Docktor, Comment, Rate, Specialty, Province, Contactdoctor


class SpecialtyInline(admin.TabularInline):
    model = Specialty
    extra = 0


class RateInline(admin.TabularInline):
    model = Rate
    extra = 0


class CityInlnline(admin.TabularInline):
    model = City
    extra = 0


class ProvinceInline(admin.TabularInline):
    model = Province
    extra = 0


# ارتباز با دکتر
class ContactdoctorInline(admin.TabularInline):
    model = Contactdoctor
    extra = 0


@admin.register(Docktor)
class DocktorAdmin(admin.ModelAdmin):
    inlines = (SpecialtyInline, ProvinceInline, ContactdoctorInline)
    list_display = ('get_full_name', 'mobile_phone', 'description_doctor', 'is_active')
    list_filter = ('is_active','create_at', 'update_at')
    list_per_page = 20
    search_fields = ('first_name', 'last_name', 'mobile_phone', 'medical_system_number')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('specialty_name', 'is_active', 'doctor')
    list_filter = ('is_active','create_at', 'update_at')
    list_per_page = 20
    search_fields = ('specialty_name',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    inlines = (CityInlnline, )
    list_per_page = 20
    list_display = ('province_name', 'is_active', 'doctor')
    search_fields = ('province_name',)
    list_filter = ('is_active','create_at', 'update_at')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'is_active', 'province')
    list_filter = ('is_active','create_at', 'update_at')
    list_per_page = 220
    search_fields = ('city_name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('title_comment', 'body_comment', 'is_active', 'doctor')
    list_filter = ('is_active','create_at', 'update_at')
    search_fields = ('title_comment', 'body_comment')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('score', 'create_at', 'update_at')
    list_per_page = 20
    list_filter = ('create_at', 'update_at')


@admin.register(Contactdoctor)
class Contactdoctor(admin.ModelAdmin):
    list_display = ('instagram', 'facebook', 'telegram', 'twitter', 'is_active')
    list_filter = ('is_active','create_at', 'update_at')
    list_per_page = 20
    search_fields = ('instagram', 'twitter')
    