from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update, SoftDelete


class Clinic(Create, Update):
    clinic_name = models.CharField(_('نام کلینیک'), max_length=100, unique=True)
    clinic_address = models.TextField(_('ادرس کلینیک'))
    clinic_postal_code = models.CharField(_('کد پستی کلینیک'), max_length=11)
    clinic_description = models.TextField(_('توضح در مورد کلینیک'))
    is_active_clinic = models.BooleanField(_('فعال کلینیک'), default=True)
    start_date = models.DateField(_('تاریخ شروع فعالیت'))
    end_date = models.DateField(_("پایان کلینیک"), blank=True, null=True)
    establishment_date = models.DateField(_('تاریخ تأسیس'))
    doctor_count = models.PositiveIntegerField(_('تعداد پزشکان'), default=0)
    staff_count = models.IntegerField(_('تعداد پرسنل'), default=0)
    
    def __str__(self) -> str:
        return self.clinic_name
    
    class Meta:
        verbose_name = _('clinic')
        verbose_name_plural = _('clinics')
        db_table = 'clinic'


class ContactClinic(Create, Update):
    landing_phone = models.CharField(_('تلفن ثابت'), max_length=11, unique=True)
    mobile_phone = models.CharField(_('تلفن موبایل'), max_length=11, unique=True)
    email = models.EmailField(_('ایمیل'), max_length=255, blank=True, null=True, unique=True)
    is_active = models.BooleanField(_('فعال بودن'), default=True)
    description = models.TextField(_('توضیح در مورد راه های ارتباطی'), blank=True, null=True)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='clinic_contact', verbose_name='کلینیک')
    
    def __str__(self) -> str:
        return f'{self.landing_phone}-- {self.mobile_phone}'
    
    class Meta:
        verbose_name = _('contact clinic')
        verbose_name_plural = _('contact clinics')
        db_table = 'contact_clinic'


class ClinicType(Create, Update):
    clinic_type = models.CharField(_('نوع کلینیک'), max_length=100, unique=True)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='clinic_type', verbose_name='کلینیک')
    
    def __str__(self) -> str:
        return self.clinic_type

    class Meta:
        verbose_name = _('clinic type')
        verbose_name_plural = _('clinic types')
        db_table = 'clinic_type'


class License(Create, Update):
    health_license = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='health_license', verbose_name='مجوز بهداشتی')
    building_permit = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='license_building_permit', verbose_name='مجوز ساختمانی')
    technical_license = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='license_technical_license', verbose_name='مجوز فنی')
    professional_license = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='professional_license', verbose_name='مجوز حرفه ای')
    safety_license = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='license_safety_license', verbose_name='مجوز ایمنی')
    clinic_id = models.ForeignKey(Clinic, on_delete=models.PROTECT, related_name='license_clinic', verbose_name='مجوز های کلینیک')
    
    class Meta:
        verbose_name = _('License')
        verbose_name_plural = _('Licenses')
        db_table = 'License'
