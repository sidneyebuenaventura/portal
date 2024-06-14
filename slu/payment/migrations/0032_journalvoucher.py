# Generated by Django 3.2.14 on 2022-07-30 17:18

from django.db import migrations, models
import slu.framework.models
import slu.framework.validators
import slu.payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0031_auto_20220730_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('file_id', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(upload_to=slu.payment.models.journal_voucher_file_path, validators=[slu.framework.validators.csv_file_validator])),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('O', 'Processing'), ('F', 'Failed'), ('C', 'Completed')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "O": "Processing",\n    "F": "Failed",\n    "C": "Completed"\n}\n```', max_length=2)),
                ('error_message', models.TextField(blank=True)),
                ('success', models.IntegerField(default=0, help_text='Successful entries')),
                ('invalid', models.IntegerField(default=0, help_text='Entries with student IDs not found')),
                ('total', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]
