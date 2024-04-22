# Generated by Django 5.0.3 on 2024-04-22 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('employment_type', models.CharField(choices=[('contractor', 'Contractor'), ('internal', 'Internal')], default='internal', max_length=20)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('v', 'Female'), ('u', 'Undefined')], default='u', max_length=10)),
                ('github_username', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
