# Generated by Django 3.2.14 on 2022-07-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_alter_accounttransaction_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='payment_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]