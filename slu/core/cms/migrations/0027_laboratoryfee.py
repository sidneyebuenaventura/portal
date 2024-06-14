# Generated by Django 3.2.13 on 2022-07-10 05:17

from django.db import migrations, models
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0026_merge_0025_auto_20220704_1424_0025_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('name', models.TextField(max_length=250)),
                ('year_start', models.PositiveIntegerField()),
                ('year_end', models.PositiveIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subjects', models.ManyToManyField(blank=True, to='core_cms.Subject')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.SoftDeleteMixin, slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]