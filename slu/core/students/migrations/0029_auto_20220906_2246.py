# Generated by Django 3.2.14 on 2022-09-06 14:46

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_students', '0028_enrolledclass_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrolledclassgrade',
            old_name='grade',
            new_name='final_grade',
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='midterm_grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='prelim_grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='enrolledclassgrade',
            name='tentative_final_grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='enrolledclassgrade',
            name='enrolled_class',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='core_students.enrolledclass'),
        ),
        migrations.AlterField(
            model_name='enrolledclassgrade',
            name='status',
            field=slu.framework.models.TextChoiceField(choices=[('PN', 'Pending'), ('P', 'Passed'), ('HP', 'High Passed'), ('INC', 'Incomplete'), ('NFE', 'No Final Examination'), ('D', 'Dropped'), ('Y', 'Yearly'), ('WP', 'Withdrawal with Permission'), ('F', 'Failed')], default='PN', help_text='```json\n{\n    "PN": "Pending",\n    "P": "Passed",\n    "HP": "High Passed",\n    "INC": "Incomplete",\n    "NFE": "No Final Examination",\n    "D": "Dropped",\n    "Y": "Yearly",\n    "WP": "Withdrawal with Permission",\n    "F": "Failed"\n}\n```', max_length=5),
        ),
    ]