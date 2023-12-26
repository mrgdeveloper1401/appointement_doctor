from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from core.models import Create, Update
from .managers import UserManagers


class users(AbstractBaseUser, PermissionsMixin, Create, Update):
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('نام خانوادگی'), max_length=100)
    email = models.EmailField(_('ایمیل'), unique=True, max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(_('شماره موبایل'), max_length=11, unique=True)
    is_active = models.BooleanField(_('کاربر فعال'), default=False, editable=False)
    is_staff = models.BooleanField(_('دسترسی کارمندی'), default=False, editable=False)
    
    objects = UserManagers()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile_phone"
    REQUIRED_FIELDS = ("email",)
    
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'user'
        
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
