from django.conf.urls import include, url
from .views import homeview, listpdf, appsview, videoview, contactview 

urlpatterns = [
    url(r"^$", homeview, name="home"),
    url(r'^listpdf/$', listpdf, name="listpdf"),
    url(r"^apps/$", appsview, name="apps"),
    url(r"^videos/$", videoview, name="videos"),
    url(r"^contact/$", contactview, name="contact"),
]