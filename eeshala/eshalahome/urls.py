from django.conf.urls import include, url
from .views import homeview

urlpatterns = [
    url(r"^$", homeview, name="home"),
]