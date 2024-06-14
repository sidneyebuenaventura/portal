# Generated by Django 3.2.14 on 2022-10-26 09:30

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0033_studentrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='studentrequest',
            name='type',
        ),
        migrations.CreateModel(
            name='AddSubjectRequest',
            fields=[
                ('studentrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_students.studentrequest')),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('IR', 'In Review'), ('A', 'Approved'), ('R', 'Rejected')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "IR": "In Review",\n    "A": "Approved",\n    "R": "Rejected"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_students.studentrequest',),
        ),
        migrations.CreateModel(
            name='ChangeScheduleRequest',
            fields=[
                ('studentrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_students.studentrequest')),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('IR', 'In Review'), ('A', 'Approved'), ('R', 'Rejected')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "IR": "In Review",\n    "A": "Approved",\n    "R": "Rejected"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_students.studentrequest',),
        ),
    ]