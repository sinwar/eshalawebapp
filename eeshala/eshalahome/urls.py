from django.conf.urls import include, url
from .views import homeview, listpdf

urlpatterns = [
    url(r"^$", homeview, name="home"),
    url(r'^listpdf/$', listpdf, name="listpdf"),
]