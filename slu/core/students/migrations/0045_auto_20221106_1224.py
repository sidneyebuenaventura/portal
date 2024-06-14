# Generated by Django 3.2.14 on 2022-11-06 04:24

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0044_withdrawalrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawalrequest',
            name='category',
            field=slu.framework.models.TextChoiceField(choices=[('FW', 'Full Withdrawal'), ('PW', 'Partial Withdrawal')], default='PW', help_text='```json\n{\n    "FW": "Full Withdrawal",\n    "PW": "Partial Withdrawal"\n}\n```', max_length=2),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='type',
            field=slu.framework.models.TextChoiceField(choices=[('PWWP', 'Partial (Within Withdrawal Period)'), ('PAWP', 'Partial (After Withdrawal Period)'), ('FWFWWP', 'Full (Within 1st Week Withdrawal Period)'), ('FWSWWP', 'Full (Within 2nd Week Withdrawal Period)'), ('FWMWP', 'Full w/ Medical Certificate (Within Prelim Exams)'), ('FWMWM', 'Full w/ Medical Certificate (Within Prelim Exams)'), ('FAWP', 'Full (After Withdrawal Period)'), ('NC', 'No charge')], default='NC', help_text='```json\n{\n    "PWWP": "Partial (Within Withdrawal Period)",\n    "PAWP": "Partial (After Withdrawal Period)",\n    "FWFWWP": "Full (Within 1st Week Withdrawal Period)",\n    "FWSWWP": "Full (Within 2nd Week Withdrawal Period)",\n    "FWMWP": "Full w/ Medical Certificate (Within Prelim Exams)",\n    "FWMWM": "Full w/ Medical Certificate (Within Prelim Exams)",\n    "FAWP": "Full (After Withdrawal Period)",\n    "NC": "No charge"\n}\n```', max_length=8),
        ),
    ]
