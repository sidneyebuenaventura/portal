# Generated by Django 3.2.13 on 2022-07-10 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0014_academicyear_semester'),
        ('core_students', '0016_enrollment_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='year_end',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='year_start',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='academic_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrollments', to='core_accounts.academicyear'),
        ),
    ]
