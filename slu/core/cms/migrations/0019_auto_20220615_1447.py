# Generated by Django 3.2.13 on 2022-06-15 14:47

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core_accounts', '0010_auto_20220610_1813'),
        ('core_cms', '0018_auto_20220614_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feespecification',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='charge_code',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='degree_type',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='total_unit_from',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='total_unit_to',
        ),
        migrations.RemoveField(
            model_name='feespecification',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=slu.framework.models.TextChoiceField(blank=True, choices=[('A', 'Associate/Certificate'), ('B', 'Bachelor Degree'), ('M', 'Masteral'), ('D', 'Doctoral'), ('P', 'Post Graduate'), ('1', 'Special Program')], help_text='```json\n{\n    "A": "Associate/Certificate",\n    "B": "Bachelor Degree",\n    "M": "Masteral",\n    "D": "Doctoral",\n    "P": "Post Graduate",\n    "1": "Special Program"\n}\n```', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='feespecification',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_core_cms.feespecification_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='feespecification',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_fee_specifications', to='core_accounts.school'),
        ),
        migrations.AddField(
            model_name='feespecification',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_fee_specifications', to='core_cms.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='charge_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=slu.framework.models.TextChoiceField(blank=True, choices=[('MLS', 'Medical Laboratory Science'), ('M', 'Masteral'), ('BA', 'Business Administration'), ('HM', 'Hospitality and Tourism Management'), ('P', 'Philosophy'), ('E', 'Education'), ('EN', 'English'), ('L', 'Law'), ('MT', 'Medical Technology'), ('ACC', 'Accountancy'), ('D', 'Doctoral'), ('MATH', 'Mathematics'), ('ENGG', 'ENGINEERING'), ('RT', 'Radiologic Technology'), ('IT', 'Info Technology'), ('C', 'Commerce'), ('ARC', 'Architecture'), ('CS', 'Computer Science'), ('AB', 'AB'), ('ECO', 'Economics'), ('LIT', 'Literature'), ('MACC', 'Management Accounting'), ('BIO', 'Biology'), ('LS', 'Legal Studies'), ('COMM', 'Communication'), ('PS', 'Political Science'), ('IS', 'Interdisciplinary Studies'), ('STAT', 'Statistics'), ('PSY', 'Psychology'), ('SW', 'Social Work'), ('SOC', 'Sociology'), ('PH', 'Pharmacy'), ('N', 'Nursing'), ('MED', 'Medicine')], help_text='```json\n{\n    "MLS": "Medical Laboratory Science",\n    "M": "Masteral",\n    "BA": "Business Administration",\n    "HM": "Hospitality and Tourism Management",\n    "P": "Philosophy",\n    "E": "Education",\n    "EN": "English",\n    "L": "Law",\n    "MT": "Medical Technology",\n    "ACC": "Accountancy",\n    "D": "Doctoral",\n    "MATH": "Mathematics",\n    "ENGG": "ENGINEERING",\n    "RT": "Radiologic Technology",\n    "IT": "Info Technology",\n    "C": "Commerce",\n    "ARC": "Architecture",\n    "CS": "Computer Science",\n    "AB": "AB",\n    "ECO": "Economics",\n    "LIT": "Literature",\n    "MACC": "Management Accounting",\n    "BIO": "Biology",\n    "LS": "Legal Studies",\n    "COMM": "Communication",\n    "PS": "Political Science",\n    "IS": "Interdisciplinary Studies",\n    "STAT": "Statistics",\n    "PSY": "Psychology",\n    "SW": "Social Work",\n    "SOC": "Sociology",\n    "PH": "Pharmacy",\n    "N": "Nursing",\n    "MED": "Medicine"\n}\n```', max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='MiscellaneousFeeSpecification',
            fields=[
                ('feespecification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_cms.feespecification')),
                ('total_unit_from', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_unit_to', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core_cms.feespecification',),
        ),
        migrations.CreateModel(
            name='OtherFeeSpecification',
            fields=[
                ('feespecification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_cms.feespecification')),
                ('student_type', slu.framework.models.TextChoiceField(blank=True, choices=[('S', 'Student'), ('FA', 'Freshmen Applicant')], help_text='```json\n{\n    "S": "Student",\n    "FA": "Freshmen Applicant"\n}\n```', max_length=5, null=True)),
                ('course_category', slu.framework.models.TextChoiceField(blank=True, choices=[('MLS', 'Medical Laboratory Science'), ('M', 'Masteral'), ('BA', 'Business Administration'), ('HM', 'Hospitality and Tourism Management'), ('P', 'Philosophy'), ('E', 'Education'), ('EN', 'English'), ('L', 'Law'), ('MT', 'Medical Technology'), ('ACC', 'Accountancy'), ('D', 'Doctoral'), ('MATH', 'Mathematics'), ('ENGG', 'ENGINEERING'), ('RT', 'Radiologic Technology'), ('IT', 'Info Technology'), ('C', 'Commerce'), ('ARC', 'Architecture'), ('CS', 'Computer Science'), ('AB', 'AB'), ('ECO', 'Economics'), ('LIT', 'Literature'), ('MACC', 'Management Accounting'), ('BIO', 'Biology'), ('LS', 'Legal Studies'), ('COMM', 'Communication'), ('PS', 'Political Science'), ('IS', 'Interdisciplinary Studies'), ('STAT', 'Statistics'), ('PSY', 'Psychology'), ('SW', 'Social Work'), ('SOC', 'Sociology'), ('PH', 'Pharmacy'), ('N', 'Nursing'), ('MED', 'Medicine')], help_text='```json\n{\n    "MLS": "Medical Laboratory Science",\n    "M": "Masteral",\n    "BA": "Business Administration",\n    "HM": "Hospitality and Tourism Management",\n    "P": "Philosophy",\n    "E": "Education",\n    "EN": "English",\n    "L": "Law",\n    "MT": "Medical Technology",\n    "ACC": "Accountancy",\n    "D": "Doctoral",\n    "MATH": "Mathematics",\n    "ENGG": "ENGINEERING",\n    "RT": "Radiologic Technology",\n    "IT": "Info Technology",\n    "C": "Commerce",\n    "ARC": "Architecture",\n    "CS": "Computer Science",\n    "AB": "AB",\n    "ECO": "Economics",\n    "LIT": "Literature",\n    "MACC": "Management Accounting",\n    "BIO": "Biology",\n    "LS": "Legal Studies",\n    "COMM": "Communication",\n    "PS": "Political Science",\n    "IS": "Interdisciplinary Studies",\n    "STAT": "Statistics",\n    "PSY": "Psychology",\n    "SW": "Social Work",\n    "SOC": "Sociology",\n    "PH": "Pharmacy",\n    "N": "Nursing",\n    "MED": "Medicine"\n}\n```', max_length=10, null=True)),
                ('subject_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_group_specifications', to='core_cms.subjectgrouping')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core_cms.feespecification',),
        ),
    ]