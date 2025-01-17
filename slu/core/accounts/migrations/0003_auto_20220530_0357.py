# Generated by Django 3.2.13 on 2022-05-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core_accounts', '0002_school_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.IntegerField(default=0, help_text='Sort index'),
        ),
        migrations.AddField(
            model_name='module',
            name='platform',
            field=models.CharField(choices=[('W', 'Web'), ('M', 'Mobile')], default='W', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module',
            name='add_permissions',
            field=models.ManyToManyField(blank=True, related_name='modules_add', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='module',
            name='change_permissions',
            field=models.ManyToManyField(blank=True, related_name='modules_change', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='module',
            name='delete_permissions',
            field=models.ManyToManyField(blank=True, related_name='modules_delete', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='module',
            name='view_permissions',
            field=models.ManyToManyField(blank=True, related_name='modules_view', to='auth.Permission'),
        ),
    ]
