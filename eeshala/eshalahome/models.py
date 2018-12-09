from django.db import models

# Create your models here.


class pdfs(models.Model):
    """
    model to save PDFs
    """
    title = models.CharField(default="pdf", max_length = 200)
    file = models.FileField(upload_to='eshalahome/static/pdf')