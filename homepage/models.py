from django.conf import settings
from django.db import models


class Homepage(models.Model):
    "Generated Model"
    user_firm = models.OneToOneField(
        "firm.Firm_companies",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_user_firm",
    )
    user_settings = models.TextField(
        null=True,
        blank=True,
    )


# Create your models here.
