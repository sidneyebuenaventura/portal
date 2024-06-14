# Generated by Django 3.2.14 on 2022-10-19 03:14

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0040_classgradestate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumsubject',
            name='tuition_fee_category',
        ),
        migrations.RemoveField(
            model_name='laboratoryfee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='laboratoryfee',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='laboratoryfee',
            name='subjects',
        ),
        migrations.AddField(
            model_name='class',
            name='tuition_fee_rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to='core_cms.tuitionfeerate'),
        ),
        migrations.AddField(
            model_name='laboratoryfee',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laboratory_fee', to='core_cms.subject'),
        ),
        migrations.AlterField(
            model_name='tuitionfeecategory',
            name='category',
            field=slu.framework.models.TextChoiceField(blank=True, choices=[('MSIT/MIT', 'MSIT/MIT'), ('D', 'Doctorate'), ('PRO', 'Professional'), ('N', 'Nursing'), ('GPM', 'Graduate Program (Masteral)'), ('LLM', 'LLM (Masteral Law)'), ('CS', 'Computer Science'), ('L', 'Law'), ('NSTP', 'NSTP'), ('MSIT', 'MSIT'), ('GP', 'Graduate Program'), ('NP', 'Non-Professional')], help_text='```json\n{\n    "MSIT/MIT": "MSIT/MIT",\n    "D": "Doctorate",\n    "PRO": "Professional",\n    "N": "Nursing",\n    "GPM": "Graduate Program (Masteral)",\n    "LLM": "LLM (Masteral Law)",\n    "CS": "Computer Science",\n    "L": "Law",\n    "NSTP": "NSTP",\n    "MSIT": "MSIT",\n    "GP": "Graduate Program",\n    "NP": "Non-Professional"\n}\n```', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tuitionfeerate',
            name='tuition_fee_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='core_cms.tuitionfeecategory'),
        ),
    ]