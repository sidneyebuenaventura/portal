# Generated by Django 3.2.14 on 2022-08-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0035_alter_curriculumsubject_curriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoryfee',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laboratoryfee',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
