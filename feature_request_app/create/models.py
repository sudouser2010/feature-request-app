from __future__ import unicode_literals

from django.db import models


class FeatureRequest(models.Model):

    class Client(object):
        A = 0
        B = 1
        C = 2

    class ProductionArea(object):
        POLICIES = 0
        BILLING = 1
        CLAIMS = 2
        REPORTS = 3

    ClientChoices = (
        (Client.A, 'A'),
        (Client.B, 'B'),
        (Client.C, 'C'),
    )

    ProductionAreaChoices = (
        (ProductionArea.POLICIES, 'Policies'),
        (ProductionArea.BILLING, 'Billing'),
        (ProductionArea.CLAIMS, 'Claims'),
        (ProductionArea.REPORTS, 'Reports'),
    )

    title = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=128, null=True)
    client = models.IntegerField(choices=ClientChoices, default=0)
    priority = models.IntegerField(default=1)
    target_date = models.DateField(null=True)
    ticket_url = models.URLField(null=True)
    product_area = models.IntegerField(choices=ProductionAreaChoices, default=0)
