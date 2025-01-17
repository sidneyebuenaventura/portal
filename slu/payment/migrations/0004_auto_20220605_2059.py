# Generated by Django 3.2.13 on 2022-06-05 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_students', '0004_auto_20220605_2059'),
        ('payment', '0003_auto_20220603_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statementofaccount',
            name='amount',
        ),
        migrations.AddField(
            model_name='statementofaccount',
            name='enrollment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statement_of_account', to='core_students.enrollment'),
        ),
        migrations.AddField(
            model_name='statementofaccount',
            name='min_amount_due',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementofaccount',
            name='total_amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statementofaccount',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statement_of_accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StatementLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=3, max_digits=9)),
                ('soa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='payment.statementofaccount')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]
