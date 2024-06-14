# Generated by Django 3.2.13 on 2022-07-02 14:38

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_alter_bukastransaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragonpaytransaction',
            name='status',
            field=slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('F', 'Failed'), ('S', 'Success'), ('ST', 'Settled')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "F": "Failed",\n    "S": "Success",\n    "ST": "Settled"\n}\n```', max_length=2),
        ),
    ]