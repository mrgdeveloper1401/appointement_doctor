from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from user.models import users


class appointmentDate(Create, Update):
    date = models.DateField(_('تاریخ'))
    from_the_time = models.TimeField(_('از ساعت'))
    at_the_time = models.TimeField(_('تا ساعت'))
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT, related_name='patient_date', verbose_name='تاریخ توبت مریض')
    def __str__(self) -> str:
        return self.date
    
    class Meta:
        verbose_name = _("appointmentDate")
        verbose_name_plural = _("appointmentDates")
        db_table = 'appointment_date'


class Patient(users, Create, Update):
    address_patient = models.TextField(_('آدرس مریض'))
    nation_code = models.CharField(_('شماره ملی مریض'), unique=True, max_length=11)
    doctor = models.ForeignKey('doctors.Docktor', on_delete=models.PROTECT, related_name='patient', verbose_name='دکتر معالج کننده')
    insurance_number = models.CharField(_('شماره بیمه'), max_length=20, blank=True, null=True)
    blood_type = models.CharField(_('گروه خون'), max_length=5, blank=True, null=True)
    allergies = models.TextField(_('حساسیت‌ها'), blank=True, null=True)
    medical_history = models.TextField(_('سوابق پزشکی'), blank=True, null=True)
    emergency_contact_name = models.CharField(_('نام شخص اضطراری'), max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(_('شماره تماس شخص اضطراری'), max_length=12, blank=True, null=True)
    occupation = models.CharField(_('شغل'), max_length=100, blank=True, null=True)
    marital_status = models.CharField(_('وضعیت تاهل'), max_length=20, blank=True, null=True)
    referred_by = models.CharField(_('ارجاع دهنده'), max_length=100, blank=True, null=True)
    height = models.DecimalField(_('قد (سانتیمتر)'), max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(_('وزن (کیلوگرم)'), max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.get_full_name} -- {self.nation_code}'

    class Meta:
        verbose_name = _("patient")
        verbose_name_plural = _("patients")
        db_table = 'patient'