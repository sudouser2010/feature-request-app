from __future__ import unicode_literals

from django.db import models

class FeatureRequest(models.Model):

    class CLIENT(object):
        A = 0
        B = 1
        C = 2

    class PRODUCTION_AREA(object):
        POLICIES = 0
        BILLING = 1
        CLAIMS = 2
        REPORTS = 3

    CLIENT_CHOICES = (
        (CLIENT.A, 'A'),
        (CLIENT.B, 'B'),
        (CLIENT.C, 'C'),
    )

    PRODUCTION_AREA_CHOICES = (
        (PRODUCTION_AREA.POLICIES, 'Policies'),
        (PRODUCTION_AREA.BILLING, 'Billing'),
        (PRODUCTION_AREA.CLAIMS, 'Claims'),
        (PRODUCTION_AREA.REPORTS, 'Reports'),
    )

    title = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=128, null=True)
    client = models.IntegerField(choices=CLIENT_CHOICES, default=0)
    priority = models.IntegerField(default=1)
    target_date = models.DateField(null=True)
    ticket_url = models.URLField(null=True)
    product_area = models.IntegerField(choices=PRODUCTION_AREA_CHOICES, default=0)

    class Meta:
        unique_together = ('client', 'priority')
