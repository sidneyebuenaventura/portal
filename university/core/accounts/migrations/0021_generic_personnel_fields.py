from django.db import migrations

import university.framework.models


class Migration(migrations.Migration):

    dependencies = [
        ("core_accounts", "0020_alter_module_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personnel",
            old_name="baguio_address",
            new_name="local_address",
        ),
        migrations.RenameField(
            model_name="personnel",
            old_name="baguio_phone_no",
            new_name="local_phone_no",
        ),
        migrations.AlterField(
            model_name="personnel",
            name="category",
            field=university.framework.models.TextChoiceField(
                choices=[
                    ("FE", "Faculty"),
                    ("CF", "Contractual Faculty"),
                    ("AE", "Admin Employee"),
                    ("CE", "Contractual Employee"),
                    ("NS", "Visiting Lecturer"),
                ],
                help_text='```json\n{\n    "FE": "Faculty",\n    "CF": "Contractual Faculty",\n    "AE": "Admin Employee",\n    "CE": "Contractual Employee",\n    "NS": "Visiting Lecturer"\n}\n```',
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="personnel",
            name="union_affiliation",
            field=university.framework.models.TextChoiceField(
                blank=True,
                choices=[("E", "ELP"), ("U", "Faculty Union"), ("A", "ALLIANCE")],
                help_text='```json\n{\n    "E": "ELP",\n    "U": "Faculty Union",\n    "A": "ALLIANCE"\n}\n```',
                max_length=50,
                null=True,
            ),
        ),
    ]
