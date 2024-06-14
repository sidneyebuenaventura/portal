# Generated by Django 3.2.13 on 2022-06-24 15:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0022_auto_20220623_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionFeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('ref_id', models.CharField(max_length=50)),
                ('year_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TuitionFeeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('year_start', models.PositiveIntegerField()),
                ('year_end', models.PositiveIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tuition_fee_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuition_fee_category_rates', to='core_cms.tuitionfeecategory')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='curriculumsubject',
            name='category_rate',
            field=slu.framework.models.TextChoiceField(blank=True, choices=[('PE', 'Professional Education'), ('NP', 'Non-Professional'), ('ITR', 'IT Rate'), ('NR', 'Nurse Rate'), ('LR', 'LLB Rate'), ('G', 'Graduate')], help_text='```json\n{\n    "PE": "Professional Education",\n    "NP": "Non-Professional",\n    "ITR": "IT Rate",\n    "NR": "Nurse Rate",\n    "LR": "LLB Rate",\n    "G": "Graduate"\n}\n```', max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='SubjectFee',
        ),
        migrations.AddField(
            model_name='curriculumsubject',
            name='tuition_fee_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculum_subjects', to='core_cms.tuitionfeecategory'),
        ),
    ]
