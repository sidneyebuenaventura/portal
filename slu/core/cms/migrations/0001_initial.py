# Generated by Django 3.2.13 on 2022-05-29 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('code', models.CharField(max_length=50)),
                ('sub_code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('major', models.CharField(blank=True, max_length=250, null=True)),
                ('minor', models.CharField(blank=True, max_length=250, null=True)),
                ('is_accredited', models.BooleanField(default=True)),
                ('accredited_year', models.IntegerField(blank=True, null=True)),
                ('has_board_exam', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('duration', models.IntegerField(default=1)),
                ('duration_unit', models.CharField(choices=[('Y', 'Year'), ('M', 'Month')], default='Y', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('semester', models.CharField(choices=[('FS', 'First Semester'), ('SS', 'Second Semester'), ('S', 'Summer')], default='FS', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CurriculumConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('effective_start_year', models.IntegerField()),
                ('effective_end_year', models.IntegerField()),
                ('effective_semester', models.CharField(choices=[('FS', 'First Semester'), ('SS', 'Second Semester'), ('S', 'Summer')], default='FS', max_length=50)),
                ('is_current', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('number', models.CharField(db_index=True, max_length=150)),
                ('description', models.TextField()),
                ('size', models.IntegerField()),
                ('floor_no', models.IntegerField()),
                ('wing', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('furniture', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_lecture_room', models.BooleanField(default=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='core_cms.building')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='core_cms.classification')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='core_accounts.school')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('type', models.CharField(choices=[('S', 'Semester'), ('T', 'Trimester')], default='S', max_length=20)),
                ('semester', models.CharField(choices=[('FS', 'First Semester'), ('SS', 'Second Semester'), ('S', 'Summer')], default='FS', max_length=20)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('confirmed_count', models.IntegerField(default=0)),
                ('reserved_count', models.IntegerField(default=0)),
                ('is_external_class', models.BooleanField(default=False)),
                ('is_dissolved', models.BooleanField(default=False)),
                ('is_crash_course', models.BooleanField(default=False)),
                ('is_global', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='YearLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('name', models.CharField(max_length=250)),
                ('course_no', models.CharField(max_length=20)),
                ('is_no_course_number', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('units', models.IntegerField(default=1)),
                ('category', models.CharField(choices=[('LEC', 'Lecture'), ('LAB', 'Laboratory')], default='LEC', max_length=20)),
                ('type', models.CharField(choices=[('N', 'None'), ('P', 'Pre-Requisite'), ('C', 'Co-Requisite')], default='N', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('type_subject', models.ManyToManyField(related_name='type_subjects', to='core_cms.Subject')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ScheduleTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('day', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday')], default='M', max_length=20)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_schedules', to='core_cms.room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduleFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('professional_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('non_professional_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('laboratory_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('addtl_laboratory_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_fees', to='core_cms.schedule')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='core_cms.subject'),
        ),
        migrations.CreateModel(
            name='CurriculumSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('lec_hrs', models.IntegerField(default=1)),
                ('lab_wk', models.IntegerField(default=1)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_subjects', to='core_cms.curriculum')),
                ('subject', models.ManyToManyField(related_name='curriculum_subjects', to='core_cms.Subject')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='configuration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_cms.curriculumconfiguration'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_curriculums', to='core_cms.course'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='year_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_cms.yearlevel'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='core_cms.coursecategory'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='core_accounts.school'),
        ),
    ]
