# Generated by Django 3.2.14 on 2022-09-27 18:38

from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_cms', '0039_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassGradeState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('prelim_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('midterm_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('tentative_final_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('final_grade_state', slu.framework.models.TextChoiceField(choices=[('E', 'Empty'), ('D', 'Draft'), ('S', 'Submitted')], default='E', help_text='```json\n{\n    "E": "Empty",\n    "D": "Draft",\n    "S": "Submitted"\n}\n```', max_length=1)),
                ('klass', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grade_states', to='core_cms.class')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]
