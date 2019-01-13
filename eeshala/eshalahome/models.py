from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class pdfs(models.Model):
    """
    model to save PDFs
    """
    title = models.CharField(default="pdf", max_length = 200)
    file = models.FileField(upload_to='eshalahome/static/pdf')


class ContactMessage(models.Model):
	"""
	model to save contact form data
	"""
	sendername = models.CharField(default="annonymous",
	 							  max_length=200,
	 							  verbose_name=_('Sender Name'))
	senderemail = models.EmailField(max_length=400,
									blank=True,
									null=True,
									verbose_name=_('Sender Email'))
	message = models.TextField(verbose_name=_('Query'),
								help_text=_('Type your query, Please be explicit'))