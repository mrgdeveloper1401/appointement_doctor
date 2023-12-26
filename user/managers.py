from typing import Any
from django.contrib.auth.models import BaseUserManager


class UserManagers(BaseUserManager):
    def create_user(self, mobile_phone, password=None):
        if not mobile_phone:
            raise ValueError('Users must have a mobile phone number')
        user = self.model(mobile_phone=mobile_phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile_phone, email, password=None):
        if not email:
            raise ValueError('Superusers must have an email address')
        email = self.normalize_email(email)
        user = self.create_user(mobile_phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user