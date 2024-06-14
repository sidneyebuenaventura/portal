# Generated by Django 3.2.14 on 2022-08-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0034_alter_curriculumperiod_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumsubject',
            name='curriculum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects', to='core_cms.curriculum'),
        ),
    ]