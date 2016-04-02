from django.conf.urls import url

from create.views import single_page_app


urlpatterns = [
    url(r'^',   single_page_app),
]
