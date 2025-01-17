# Generated by Django 3.2.13 on 2022-06-12 17:48

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0006_alter_enrollmentsubjectschedule_subject_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='step',
            field=slu.framework.models.TextChoiceField(choices=[(0, 'Start'), (1, 'Information'), (2, 'Discounts'), (3, 'Subjects'), (4, 'Payment'), (5, 'Enrollment Status')], default=0, help_text='```json\n{\n    "0": "Start",\n    "1": "Information",\n    "2": "Discounts",\n    "3": "Subjects",\n    "4": "Payment",\n    "5": "Enrollment Status"\n}\n```', max_length=2),
        ),
    ]
