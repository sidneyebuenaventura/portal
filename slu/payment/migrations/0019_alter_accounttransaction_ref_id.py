# Generated by Django 3.2.13 on 2022-07-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_accounttransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttransaction',
            name='ref_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]