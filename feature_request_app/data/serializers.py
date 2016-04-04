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

    def validate(self, data):
        if data['priority'] and data['client']:
            number_of_clients_for_type = FeatureRequest.objects.filter(
                client=data['client']
            ).count()
            if data['priority'] > number_of_clients_for_type:
                client = FeatureRequest.ClientChoices[data['client']][1]
                message = 'Priority can not exceed number of client {}'.format(client)
                raise serializers.ValidationError(message)

        return data
