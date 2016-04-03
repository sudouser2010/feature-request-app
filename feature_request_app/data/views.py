from rest_framework import viewsets
from rest_framework.response import Response

from create.models import FeatureRequest
from .serializers import FeatureRequestSerializer


class FeatureRequestViewset(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer

    def list(self, request):
        data = dict()
        for client in FeatureRequest.ClientChoices:
            client_data = FeatureRequest.objects.filter(
                client=client[0]
            ).values()
            data[client[1]] = client_data
        return Response(data)
