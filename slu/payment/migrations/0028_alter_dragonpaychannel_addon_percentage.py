# Generated by Django 3.2.14 on 2022-07-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0027_paymentsettlement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragonpaychannel',
            name='addon_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
