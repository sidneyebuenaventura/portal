# Generated by Django 3.2.13 on 2022-06-07 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20220605_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementofaccount',
            name='min_amount_due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dragonpaytransaction',
            name='channel_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dragonpaytransaction',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dragonpaytransaction',
            name='settlement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]