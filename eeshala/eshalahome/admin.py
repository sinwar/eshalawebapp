from django.contrib import admin

# Register your models here.
from .models import pdfs, ContactMessage

admin.site.register(pdfs)
admin.site.register(ContactMessage)