from django.db.models.expressions import F
from rest_framework import viewsets, status
from rest_framework.response import Response

from create.models import FeatureRequest
from .serializers import FeatureRequestSerializer


class FeatureRequestViewset(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer

    def list(self, request, *args, **kwargs):
        data = dict()
        for client in FeatureRequest.ClientChoices:
            client_data = FeatureRequest.objects.filter(
                client=client[0]
            ).order_by('priority').values()
            data[client[1]] = client_data
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.reorder_feature_requests(serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def reorder_feature_requests(self, serializer):
        """
            This gets all the feature requests with an equal or lower priority for a given client
            and reduces the priority of those feature requests by one.

            This makes space so the new feature request can be inserted at priority.
        """
        client = serializer.validated_data['client']
        priority = serializer.validated_data['priority']
        affected_feature_requests = FeatureRequest.objects.filter(
            client=client,
            priority__gte=priority
        )
        affected_feature_requests.update(priority=F('priority')+1)
