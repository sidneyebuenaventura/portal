# Generated by Django 3.2.14 on 2022-09-26 00:16

from django.db import migrations, models
import django.db.models.deletion
import slu.core.students.models
import slu.framework.models
import slu.framework.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0038_auto_20220917_0049'),
        ('core_students', '0030_student_emergency_contact_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('file_id', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(upload_to=slu.core.students.models.grade_sheet_file_path, validators=[slu.framework.validators.excel_file_validator])),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('O', 'Processing'), ('F', 'Failed'), ('C', 'Completed')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "O": "Processing",\n    "F": "Failed",\n    "C": "Completed"\n}\n```', max_length=2)),
                ('error_message', models.TextField(blank=True)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_sheets', to='core_cms.class')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='enrolledclass',
            options={'verbose_name_plural': 'Enrolled classes'},
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='final_grade_state',
            field=slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1),
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='midterm_grade_state',
            field=slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1),
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='prelim_grade_state',
            field=slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1),
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='tentative_final_grade_state',
            field=slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1),
        ),
        migrations.CreateModel(
            name='GradeSheetRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('prelim_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('midterm_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tentative_final_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('final_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('prelim_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('midterm_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('tentative_final_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('final_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('status', slu.framework.models.TextChoiceField(choices=[('PN', 'Pending'), ('P', 'Passed'), ('HP', 'High Passed'), ('INC', 'Incomplete'), ('NFE', 'No Final Examination'), ('D', 'Dropped'), ('Y', 'Yearly'), ('WP', 'Withdrawal with Permission'), ('F', 'Failed')], default='PN', help_text='```json\n{\n    "PN": "Pending",\n    "P": "Passed",\n    "HP": "High Passed",\n    "INC": "Incomplete",\n    "NFE": "No Final Examination",\n    "D": "Dropped",\n    "Y": "Yearly",\n    "WP": "Withdrawal with Permission",\n    "F": "Failed"\n}\n```', max_length=5)),
                ('grade_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='core_students.gradesheet')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core_students.student')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]
