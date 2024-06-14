# Generated by Django 3.2.13 on 2022-07-28 13:29

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0021_alter_enrollment_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='enrollment_remarks',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='enrollment_status',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='is_for_manual_tagging',
        ),
        migrations.RemoveField(
            model_name='student',
            name='enrollment_status',
        ),
        migrations.CreateModel(
            name='EnrollmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('block_status', slu.framework.models.TextChoiceField(blank=True, choices=[('P', 'Passed'), ('BWOB', 'Blocked with Outstanding Balance'), ('BWFS', 'Blocked with Failed Subject'), ('BWOBFG', 'Blocked with Outstanding Balance and Failed Grade')], help_text='```json\n{\n    "P": "Passed",\n    "BWOB": "Blocked with Outstanding Balance",\n    "BWFS": "Blocked with Failed Subject",\n    "BWOBFG": "Blocked with Outstanding Balance and Failed Grade"\n}\n```', max_length=10, null=True)),
                ('is_for_manual_tagging', models.BooleanField(default=False)),
                ('is_temporary_allowed', models.BooleanField(default=False)),
                ('evaluation_remarks', models.TextField(blank=True, null=True)),
                ('remark_code', slu.framework.models.TextChoiceField(blank=True, choices=[('FCC', 'For Curriculum Change'), ('ATE', 'Allowed to Enroll')], help_text='```json\n{\n    "FCC": "For Curriculum Change",\n    "ATE": "Allowed to Enroll"\n}\n```', max_length=10, null=True)),
                ('enrollment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core_students.enrollment')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]