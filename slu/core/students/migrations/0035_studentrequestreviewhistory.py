# Generated by Django 3.2.14 on 2022-10-26 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import slu.framework.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_students', '0034_auto_20221026_1730'),
    ]

    operations = [
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
