# Generated by Django 3.2.13 on 2022-05-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('action', models.CharField(choices=[('c', 'Created'), ('u', 'Updated'), ('d', 'Deleted')], max_length=2)),
                ('description', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]