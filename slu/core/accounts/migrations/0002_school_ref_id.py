# Generated by Django 3.2.13 on 2022-05-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='ref_id',
            field=models.CharField(default='code', max_length=50),
            preserve_default=False,
        ),
    ]
