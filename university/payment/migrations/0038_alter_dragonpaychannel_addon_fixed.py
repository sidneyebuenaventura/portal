from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0037_paymenttransaction_error_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dragonpaychannel",
            name="addon_fixed",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Fixed institution charge",
                max_digits=9,
            ),
        ),
    ]
