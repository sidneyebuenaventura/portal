# Generated by Django 3.2.14 on 2022-09-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0033_dragonpaykey'),
    ]

    operations = [
        migrations.AddField(
            model_name='dragonpaychannel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
    ]