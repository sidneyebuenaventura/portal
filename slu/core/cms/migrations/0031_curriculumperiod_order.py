# Generated by Django 3.2.13 on 2022-07-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0030_auto_20220724_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculumperiod',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
