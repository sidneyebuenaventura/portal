from django.core.management.base import BaseCommand

from slu.core.accounts.models import Module
from slu.core.maintenance.models import ModuleConfiguration


class Command(BaseCommand):
    help = "Creates default core_maintenance.ModuleConfiguration data"

    def handle(self, *args, **options):
        configs = [
            {
                "module": "mobile.enrollment",
                "description": (
                    "Create a schedule per school, course and year level to enable "
                    "Enrollment Module"
                ),
            },
            {
                "module": "mobile.pre_enrollment",
                "description": (
                    "Create a schedule per school, course and year level to enable "
                    "Pre-Enrollment Module"
                ),
            },
        ]

        for config in configs:
            module_codename = config.pop("module")
            module = Module.objects.filter(codename=module_codename).first()

            if module:
                ModuleConfiguration.objects.update_or_create(
                    module=module, defaults=config
                )
