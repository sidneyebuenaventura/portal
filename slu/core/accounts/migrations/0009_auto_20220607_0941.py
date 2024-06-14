# Generated by Django 3.2.13 on 2022-06-07 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0008_personnel'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='emp_id',
            field=models.CharField(db_index=True, default='code', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_heads', to='core_accounts.personnel'),
        ),
    ]
