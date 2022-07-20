from django.conf import settings
from django.db import models


class Company1(models.Model):
    "Generated Model"
    company_name = models.TextField()
    portfolio_company_user = models.TextField()
    dollars_invested = models.BigIntegerField()


# Create your models here.
