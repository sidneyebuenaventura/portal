# Generated by Django 3.2.13 on 2022-06-25 03:11

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0011_auto_20220623_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='rank',
            field=slu.framework.models.TextChoiceField(blank=True, choices=[('O', 'Officer'), ('S', 'Supervisor'), ('M', 'Manager')], help_text='```json\n{\n    "O": "Officer",\n    "S": "Supervisor",\n    "M": "Manager"\n}\n```', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Rank',
        ),
    ]