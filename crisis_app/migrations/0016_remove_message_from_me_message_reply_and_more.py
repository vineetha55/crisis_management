# Generated by Django 4.1.5 on 2024-04-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_app', '0015_rename_email_tbl_feedback_view_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='from_me',
        ),
        migrations.AddField(
            model_name='message',
            name='reply',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
