# Generated by Django 3.2.13 on 2022-07-25 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0014_academicyear_semester'),
        ('core_maintenance', '0002_auto_20220623_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollmentschedule',
            name='school_year_from',
        ),
        migrations.RemoveField(
            model_name='enrollmentschedule',
            name='school_year_to',
        ),
        migrations.AddField(
            model_name='enrollmentschedule',
            name='academic_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_schedules', to='core_accounts.academicyear'),
        ),
        migrations.AlterField(
            model_name='enrollmentschedule',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_schedules', to='core_accounts.semester'),
        ),
    ]