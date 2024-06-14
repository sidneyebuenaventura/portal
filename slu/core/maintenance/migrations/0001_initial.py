# Generated by Django 3.2.13 on 2022-06-18 01:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_accounts', '0010_auto_20220610_1813'),
        ('core_cms', '0020_auto_20220617_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('school_year_from', models.IntegerField()),
                ('school_year_to', models.IntegerField()),
                ('semester', slu.framework.models.TextChoiceField(choices=[('FS', 'First Semester'), ('SS', 'Second Semester'), ('S', 'Summer')], help_text='```json\n{\n    "FS": "First Semester",\n    "SS": "Second Semester",\n    "S": "Summer"\n}\n```', max_length=2)),
                ('student_type', slu.framework.models.TextChoiceField(blank=True, choices=[('R', 'Regular'), ('S', 'Scholar'), ('I', 'International')], help_text='```json\n{\n    "R": "Regular",\n    "S": "Scholar",\n    "I": "International"\n}\n```', max_length=2)),
                ('year_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ModuleConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('module', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core_accounts.module')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EnrollmentScheduleEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('event', models.CharField(max_length=255)),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core_maintenance.enrollmentschedule')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='enrollmentschedule',
            name='config',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrollment_schedules', to='core_maintenance.moduleconfiguration'),
        ),
        migrations.AddField(
            model_name='enrollmentschedule',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_schedules', to='core_cms.course'),
        ),
        migrations.AddField(
            model_name='enrollmentschedule',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_schedules', to='core_accounts.school'),
        ),
    ]
