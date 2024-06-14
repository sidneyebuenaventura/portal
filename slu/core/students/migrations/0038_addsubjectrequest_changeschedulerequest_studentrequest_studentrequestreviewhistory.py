# Generated by Django 3.2.14 on 2022-10-26 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('core_students', '0037_auto_20221026_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('request_no', models.CharField(max_length=255, null=True)),
                ('detail', models.TextField()),
                ('reason', models.TextField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_core_students.studentrequest_set+', to='contenttypes.contenttype')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='core_students.student')),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AddSubjectRequest',
            fields=[
                ('studentrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_students.studentrequest')),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('IR', 'In Review'), ('A', 'Approved'), ('R', 'Rejected')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "IR": "In Review",\n    "A": "Approved",\n    "R": "Rejected"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_students.studentrequest',),
        ),
        migrations.CreateModel(
            name='ChangeScheduleRequest',
            fields=[
                ('studentrequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_students.studentrequest')),
                ('status', slu.framework.models.TextChoiceField(choices=[('P', 'Pending'), ('IR', 'In Review'), ('A', 'Approved'), ('R', 'Rejected')], default='P', help_text='```json\n{\n    "P": "Pending",\n    "IR": "In Review",\n    "A": "Approved",\n    "R": "Rejected"\n}\n```', max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_students.studentrequest',),
        ),
        migrations.CreateModel(
            name='StudentRequestReviewHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('remarks', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_histories', to='core_students.studentrequest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(slu.framework.models.BaseModelMixin, models.Model),
        ),
    ]