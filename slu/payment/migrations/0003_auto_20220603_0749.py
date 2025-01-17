# Generated by Django 3.2.13 on 2022-06-03 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_bukastransaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bukastransaction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='dragonpaytransaction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='bukastransaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bukastransaction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bukastransaction',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='dragonpaytransaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dragonpaytransaction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dragonpaytransaction',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='StatementOfAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_payment.paymenttransaction_set+', to='contenttypes.contenttype')),
                ('soa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payment.statementofaccount')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='bukastransaction',
            name='paymenttransaction_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.paymenttransaction'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dragonpaytransaction',
            name='paymenttransaction_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.paymenttransaction'),
            preserve_default=False,
        ),
    ]
