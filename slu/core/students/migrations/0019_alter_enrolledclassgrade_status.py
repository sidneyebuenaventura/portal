# Generated by Django 3.2.14 on 2022-07-24 20:19

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0018_auto_20220724_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledclassgrade',
            name='status',
            field=slu.framework.models.TextChoiceField(choices=[('PN', 'Pending'), ('P', 'Passed'), ('Y', 'Yearly'), ('F', 'Failed'), ('INC', 'Incomplete'), ('W', 'Withdrawn'), ('UW', 'Unauthorized Withdrawal')], help_text='```json\n{\n    "PN": "Pending",\n    "P": "Passed",\n    "Y": "Yearly",\n    "F": "Failed",\n    "INC": "Incomplete",\n    "W": "Withdrawn",\n    "UW": "Unauthorized Withdrawal"\n}\n```', max_length=5),
        ),
    ]