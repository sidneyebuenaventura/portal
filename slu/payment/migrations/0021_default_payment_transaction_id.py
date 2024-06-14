from django.conf import settings
from django.db import migrations
from hashids import Hashids

HASHIDS = Hashids(
    settings.HASHIDS_PAYMENT_SALT,
    min_length=6,
    alphabet=settings.HASHIDS_ALPHABET_DEFAULT,
)


def generate_payment_id_for_existing_transactions(apps, schema_editor):
    PaymentTransaction = apps.get_model("payment", "PaymentTransaction")
    db_alias = schema_editor.connection.alias
    transactions = PaymentTransaction.objects.using(db_alias).filter(
        payment_id__isnull=True
    )

    for transaction in transactions:
        transaction.payment_id = HASHIDS.encode(transaction.id)
        transaction.save()


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0020_paymenttransaction_payment_id"),
    ]

    operations = [
        migrations.RunPython(
            generate_payment_id_for_existing_transactions, migrations.RunPython.noop
        )
    ]
