# Generated by Django 3.2.13 on 2022-06-24 04:08

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_remove_dragonpaytransaction_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashierTransaction',
            fields=[
                ('paymenttransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.paymenttransaction')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True)),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('F', 'Failed'), ('S', 'Success')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "F": "Failed",\n    "S": "Success"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('payment.paymenttransaction',),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]