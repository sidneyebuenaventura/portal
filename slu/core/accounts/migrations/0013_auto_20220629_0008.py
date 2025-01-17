# Generated by Django 3.2.13 on 2022-06-28 16:08

from django.db import migrations
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0012_auto_20220625_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='employee_type',
            new_name='employment_type',
        ),
        migrations.AddField(
            model_name='personnel',
            name='category',
            field=slu.framework.models.TextChoiceField(choices=[('FE', 'Faculty'), ('CF', 'Contractual Faculty'), ('AE', 'Admin Employee'), ('CE', 'Contractual Employee'), ('NS', 'Non-SLU/Visiting Lecturer')], default='AE', help_text='```json\n{\n    "FE": "Faculty",\n    "CF": "Contractual Faculty",\n    "AE": "Admin Employee",\n    "CE": "Contractual Employee",\n    "NS": "Non-SLU/Visiting Lecturer"\n}\n```', max_length=50),
            preserve_default=False,
        ),
    ]
