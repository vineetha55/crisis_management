
# Generated by Django 5.0 on 2024-02-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_app', '0008_tbl_user_registration_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.CharField(max_length=100, null=True)),
                ('incident_time', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
