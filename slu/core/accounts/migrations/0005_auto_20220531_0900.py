# Generated by Django 3.2.13 on 2022-05-31 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core_accounts', '0004_auto_20220531_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='roles',
            field=models.ManyToManyField(related_name='modules', through='core_accounts.RoleModule', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='rolemodule',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='userschoolgroup',
            name='roles',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
