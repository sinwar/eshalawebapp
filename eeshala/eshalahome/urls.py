from django.conf.urls import include, url
from django.views.generic import TemplateView
from .views import homeview, listpdf, appsview, videoview, contactview, ContactMessageCreate

urlpatterns = [
    url(r"^$", homeview, name="home"),
    url(r'^listpdf/$', listpdf, name="listpdf"),
    url(r"^apps/$", appsview, name="apps"),
    url(r"^videos/$", videoview, name="videos"),
    url(r"^contact/$", ContactMessageCreate.as_view(), name="contact"),
    url(r"^contacted/$",TemplateView.as_view(template_name = "contacted.html"), name="contacted"),
]