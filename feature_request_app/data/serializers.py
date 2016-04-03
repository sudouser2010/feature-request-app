from rest_framework import serializers

from create.models import FeatureRequest


class FeatureRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeatureRequest
        fields = (
            'title',
            'description',
            'client',
            'priority',
            'target_date',
            'ticket_url',
            'product_area'
        )
