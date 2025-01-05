# Generated by Django 5.1.4 on 2025-01-05 13:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField(default='')),
                ('profile_photo', models.ImageField(upload_to='uploads/')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
