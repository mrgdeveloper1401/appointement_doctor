from django.db import models
from django.utils.translation import gettext_lazy as _


class Create(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Update(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    delete_at = models.DateTimeField(auto_now_add=True)
