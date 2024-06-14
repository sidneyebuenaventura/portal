# Generated by Django 3.2.14 on 2022-11-01 04:57

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_accounts', '0020_alter_module_category'),
        ('core_cms', '0041_auto_20221019_1114'),
        ('core_students', '0039_student_slu_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_slu_employee', models.BooleanField(default=False)),
                ('is_employee_dependent', models.BooleanField(default=False)),
                ('dependent_relationship', slu.framework.models.TextChoiceField(blank=True, choices=[('F', 'Father'), ('M', 'Mother')], help_text='```json\n{\n    "F": "Father",\n    "M": "Mother"\n}\n```', max_length=2, null=True)),
                ('is_working_scholar', models.BooleanField(default=False)),
                ('has_enrolled_sibling', models.BooleanField(default=False)),
                ('dependent_personnel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_employee_dependent_discounts', to='core_accounts.personnel')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='dependent_employee_no',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='dependent_relationship',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='is_employee_dependent',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='home_contact_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='SiblingDiscount',
        ),
        migrations.AddField(
            model_name='enrollmentdiscount',
            name='enrollment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='core_students.enrollment'),
        ),
        migrations.AddField(
            model_name='enrollmentdiscount',
            name='personnel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_employee_discounts', to='core_accounts.personnel'),
        ),
        migrations.AddField(
            model_name='enrollmentdiscount',
            name='siblings',
            field=models.ManyToManyField(blank=True, related_name='sibling_discounts', to='core_students.Student'),
        ),
        migrations.AddField(
            model_name='enrollmentdiscount',
            name='validated_discount',
            field=models.ForeignKey(blank=True, help_text='Validated discount that should be reflected on SOA', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discount_enrollments', to='core_cms.discount'),
        ),
    ]
