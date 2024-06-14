# Generated by Django 3.2.14 on 2022-09-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0016_user_is_first_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='id_code',
        ),
        migrations.AlterField(
            model_name='personnel',
            name='ref_id',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]