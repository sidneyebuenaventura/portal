# Generated by Django 3.2.13 on 2022-06-10 21:54

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20220608_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverTheCounterTransaction',
            fields=[
                ('paymenttransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.paymenttransaction')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True)),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('F', 'Failed'), ('S', 'Success')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "F": "Failed",\n    "S": "Success"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('payment.paymenttransaction',),
        ),
        migrations.AddField(
            model_name='dragonpaytransaction',
            name='meta',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
