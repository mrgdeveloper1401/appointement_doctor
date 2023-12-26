from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Create, Update
from user.models import users

# دکتر
class Docktor(users, Create, Update):
    image = models.ForeignKey('image.Images', on_delete=models.PROTECT, related_name='doctor_images', verbose_name='عکس دکتر')
    description_doctor = models.TextField(_('درمورد دکتر'))
    slug = models.SlugField(max_length=155, unique=True, allow_unicode=True)
    medical_system_number = models.CharField(_('شماره نطام پژشکی'), max_length=5, unique=True)

    class Meta:
        verbose_name = _("docktor")
        verbose_name_plural = _("docktors")
        db_table = 'docktor'

    def __str__(self) -> str:
        return self.get_full_name()


# تخصص دکتر
class Specialty(Create, Update):
    specialty_name = models.CharField(_('متخصص'), max_length=155, unique=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    doctor = models.ForeignKey(Docktor, on_delete=models.PROTECT, related_name='specialty', verbose_name='دکتر')
    
    def __str__(self) -> str:
        return self.specialty_name

    class Meta:
        verbose_name = _("specialty")
        verbose_name_plural = _("specialties")
        db_table = 'specialty'

    
# استان 
class Province(Create, Update):
    province_name = models.CharField(_('استان'), max_length=155, unique=True, db_index=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    doctor = models.ForeignKey(Docktor, on_delete=models.PROTECT, related_name='province', verbose_name='دکتر')
    
    def __str__(self) -> str:
        return self.province_name
    
    class Meta:
        verbose_name = _("province")
        verbose_name_plural = _("provinces")
        db_table = 'province'

# شهر
class City(Create, Update):
    city_name = models.CharField(_('شهر'), max_length=155, unique=True, db_index=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, related_name='cities', verbose_name='استان')
    
    def __str__(self) -> str:
        return self.city_name
    
    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")
        db_table = 'city'


# نظر
class Comment(Create, Update):
    title_comment = models.CharField(_('عنوان نظر'), max_length=155)
    body_comment = models.TextField(_('متن نظر'))
    slug = models.SlugField(max_length=155, unique=True, allow_unicode=True)
    is_active = models.BooleanField(_('فعال'), default=False)
    doctor = models.ForeignKey(Docktor, on_delete=models.PROTECT, related_name='comment', verbose_name='دکتر')
    
    def __str__(self) -> str:
        return self.title_comment
    
    class Meta:
        verbose_name = 'comment doctor'
        verbose_name_plural = 'comments doctor'
        db_table = 'comment'

# امتیاز
class Rate(Create, Update):
    score = models.PositiveSmallIntegerField(_('امتیاز'), default=0, choices=[(i, i)for i in range(1,6)])
    
    def __str__(self) -> str:
        return self.score
    
    class Meta:
        verbose_name = 'rate'
        verbose_name_plural = 'rates'
        db_table = 'rates'


# ارتباز با دکتر
class Contactdoctor(Create, Update):
    instagram = models.URLField(_('اینستاگرام'), blank=True, null=True)
    facebook = models.URLField(_('فیسبوک'), blank=True, null=True)
    telegram = models.URLField(_('تلگرام'), blank=True, null=True)
    twitter = models.URLField(_('تویتر'), blank=True, null=True)
    is_active = models.BooleanField(_('فعال'), default=True)
    doctor = models.ForeignKey(Docktor, on_delete=models.PROTECT, related_name='contact_doctor', verbose_name='دکتر')
    
    class Meta:
        verbose_name = 'contact doctor'
        verbose_name_plural = 'contact doctors'
        db_table = 'contact'
