# Generated by Django 5.0 on 2023-12-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=False, editable=False, verbose_name='کاربر فعال'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, editable=False, verbose_name='دسترسی کارمندی'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, editable=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]