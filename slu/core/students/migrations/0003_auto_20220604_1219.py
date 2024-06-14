# Generated by Django 3.2.13 on 2022-06-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0002_auto_20220602_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_previous_number',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='senior_high_strand',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
