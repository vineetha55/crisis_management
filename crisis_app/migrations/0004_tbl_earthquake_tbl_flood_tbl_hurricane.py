# Generated by Django 5.0 on 2024-01-25 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_app', '0003_tbl_disaster_manage'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_earthquake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earthquake_name', models.CharField(max_length=100, null=True)),
                ('date', models.IntegerField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('magnitude_depth', models.CharField(max_length=100, null=True)),
                ('epicenter_cordinate', models.CharField(max_length=100, null=True)),
                ('affected_area', models.CharField(max_length=100, null=True)),
                ('injuries', models.IntegerField(max_length=100, null=True)),
                ('structural_damage', models.IntegerField(max_length=100, null=True)),
                ('aftershoks', models.IntegerField(max_length=100, null=True)),
                ('relief_effort', models.IntegerField(max_length=100, null=True)),
                ('source_reference', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_flood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.IntegerField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('severity_level', models.CharField(max_length=100, null=True)),
                ('river_level_rainfall', models.IntegerField(max_length=100, null=True)),
                ('affected_area', models.CharField(max_length=100, null=True)),
                ('injuries', models.IntegerField(max_length=100, null=True)),
                ('infrstructure_damage', models.IntegerField(max_length=100, null=True)),
                ('evacuations_rescues', models.IntegerField(max_length=100, null=True)),
                ('relief_effort', models.IntegerField(max_length=100, null=True)),
                ('update_change', models.IntegerField(max_length=100, null=True)),
                ('source_reference', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_hurricane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hurricane_name', models.CharField(max_length=100, null=True)),
                ('date', models.IntegerField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('wind_speed_category', models.CharField(max_length=100, null=True)),
                ('storm_surge_rainfall', models.IntegerField(max_length=100, null=True)),
                ('affected_area', models.CharField(max_length=100, null=True)),
                ('injuries', models.IntegerField(max_length=100, null=True)),
                ('structural_damage', models.IntegerField(max_length=100, null=True)),
                ('shelter_information', models.IntegerField(max_length=100, null=True)),
                ('relief_effort', models.IntegerField(max_length=100, null=True)),
                ('update_change', models.IntegerField(max_length=100, null=True)),
                ('source_reference', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
