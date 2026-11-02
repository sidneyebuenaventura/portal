from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core_students", "0045_auto_20221106_1224"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="baguio_address",
            new_name="local_address",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="baguio_phone_no",
            new_name="local_phone_no",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="slu_email",
            new_name="institutional_email",
        ),
        migrations.RenameField(
            model_name="enrollment",
            old_name="slu_email",
            new_name="institutional_email",
        ),
        migrations.RenameField(
            model_name="enrollmentdiscount",
            old_name="is_slu_employee",
            new_name="is_employee",
        ),
    ]
