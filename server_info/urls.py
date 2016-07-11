from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.server_info, name='server_info'),
]