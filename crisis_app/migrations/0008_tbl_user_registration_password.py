# Generated by Django 5.0 on 2024-02-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_app', '0007_tbl_user_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user_registration',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]