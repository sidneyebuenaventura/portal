# Generated by Django 3.2.13 on 2022-06-24 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_auto_20220623_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dragonpaytransaction',
            name='datetime',
        ),
    ]