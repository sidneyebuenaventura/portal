# Generated by Django 3.2.14 on 2022-08-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0033_alter_class_class_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculumperiod',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
