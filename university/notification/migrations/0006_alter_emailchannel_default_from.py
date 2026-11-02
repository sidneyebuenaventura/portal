from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notification", "0005_emailchannel_enable_whitelist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailchannel",
            name="default_from",
            field=models.CharField(default="university@localhost", max_length=255),
        ),
    ]
