from django.conf.urls import url, include
from rest_framework import routers

from create.views import single_page_app
from data.views import FeatureRequestViewset


router = routers.DefaultRouter()
router.register(r'feature-requests', FeatureRequestViewset)

urlpatterns = [

    url(r'^api/', include(router.urls)),
    url(r'^',   single_page_app),
]
