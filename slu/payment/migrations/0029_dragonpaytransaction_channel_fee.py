# Generated by Django 3.2.14 on 2022-07-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0028_alter_dragonpaychannel_addon_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragonpaytransaction',
            name='channel_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]