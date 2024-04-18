# Generated by Django 5.0 on 2024-02-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_app', '0009_tbl_incident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_incident',
            old_name='password',
            new_name='incident_description',
        ),
        migrations.AddField(
            model_name='tbl_incident',
            name='injuries',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
