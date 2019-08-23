from django.conf.urls import url
from apps.principal.views import index, registro

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^registro/', registro, name='registro')
]