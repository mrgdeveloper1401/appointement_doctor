# Generated by Django 5.0 on 2023-12-26 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('user', '0003_alter_users_is_active_alter_users_is_staff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('score', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='امتیاز')),
            ],
            options={
                'verbose_name': 'rate',
                'verbose_name_plural': 'rates',
                'db_table': 'rates',
            },
        ),
        migrations.CreateModel(
            name='Docktor',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description_doctor', models.TextField(verbose_name='درمورد دکتر')),
                ('slug', models.SlugField(allow_unicode=True, max_length=155, unique=True)),
                ('medical_system_number', models.CharField(max_length=5, unique=True, verbose_name='شماره نطام پژشکی')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_images', to='image.images', verbose_name='عکس دکتر')),
            ],
            options={
                'verbose_name': 'docktor',
                'verbose_name_plural': 'docktors',
                'db_table': 'docktor',
            },
            bases=('user.users', models.Model),
        ),
        migrations.CreateModel(
            name='Contactdoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('instagram', models.URLField(verbose_name='اینستاگرام')),
                ('facebook', models.URLField(verbose_name='فیسبوک')),
                ('telegram', models.URLField(verbose_name='تلگرام')),
                ('twitter', models.URLField(verbose_name='تویتر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact_doctor', to='doctors.docktor', verbose_name='دکتر')),
            ],
            options={
                'verbose_name': 'contact doctor',
                'verbose_name_plural': 'contact doctors',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title_comment', models.CharField(max_length=155, verbose_name='عنوان نظر')),
                ('body_comment', models.TextField(verbose_name='متن نظر')),
                ('slug', models.SlugField(allow_unicode=True, max_length=155, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='doctors.docktor', verbose_name='دکتر')),
            ],
            options={
                'verbose_name': 'comment doctor',
                'verbose_name_plural': 'comments doctor',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('province_name', models.CharField(db_index=True, max_length=155, unique=True, verbose_name='استان')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='province', to='doctors.docktor', verbose_name='دکتر')),
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'provinces',
                'db_table': 'province',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('city_name', models.CharField(db_index=True, max_length=155, unique=True, verbose_name='شهر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='doctors.province', verbose_name='استان')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('specialty_name', models.CharField(max_length=155, unique=True, verbose_name='متخصص')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specialty', to='doctors.docktor', verbose_name='دکتر')),
            ],
            options={
                'verbose_name': 'specialty',
                'verbose_name_plural': 'specialties',
                'db_table': 'specialty',
            },
        ),
    ]