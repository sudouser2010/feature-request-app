from rest_framework import viewsets

from create.models import FeatureRequest
from .serializers import FeatureRequestSerializer


class FeatureRequestViewset(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
