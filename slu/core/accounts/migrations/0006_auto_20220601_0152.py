# Generated by Django 3.2.13 on 2022-06-01 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0005_auto_20220531_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='is_active',
        ),
        migrations.AddField(
            model_name='department',
            name='code',
            field=models.CharField(db_index=True, default='code', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_heads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='division_group',
            field=models.CharField(choices=[('1', 'Tertiary'), ('2', 'Hospital'), ('3', 'Elementary'), ('4', 'High School')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='department',
            name='main_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_departments', to='core_accounts.department'),
        ),
        migrations.AddField(
            model_name='department',
            name='ref_id',
            field=models.CharField(db_index=True, default='code', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_departments', to='core_accounts.school'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
