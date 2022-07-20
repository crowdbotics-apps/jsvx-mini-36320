from django.conf import settings
from django.db import models


class Firm_companies(models.Model):
    "Generated Model"
    company1 = models.OneToOneField(
        "company1.Company1",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="firm_companies_company1",
    )
    company2 = models.OneToOneField(
        "company2.Company2",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="firm_companies_company2",
    )
    company3 = models.OneToOneField(
        "company3.Company3",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="firm_companies_company3",
    )


# Create your models here.
