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
        (CLIENT.A, 'a'),
        (CLIENT.B, 'b'),
        (CLIENT.C, 'c'),
    )

    PRODUCTION_AREA_CHOICES = (
        (PRODUCTION_AREA.POLICIES, 'policies'),
        (PRODUCTION_AREA.BILLING, 'billing'),
        (PRODUCTION_AREA.CLAIMS, 'claims'),
        (PRODUCTION_AREA.REPORTS, 'reports'),
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
