# Generated by Django 3.2.14 on 2022-07-25 23:32

from django.db import migrations, models
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0022_auto_20220726_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashiertransaction',
            name='settled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cashiertransaction',
            name='status',
            field=slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('F', 'Failed'), ('V', 'Voided'), ('S', 'Paid'), ('SS', 'Settled')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "F": "Failed",\n    "V": "Voided",\n    "S": "Paid",\n    "SS": "Settled"\n}\n```', max_length=2),
        ),
    ]