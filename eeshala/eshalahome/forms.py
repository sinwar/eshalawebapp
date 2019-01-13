from django import forms
import re
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from . import models

alnum_re = re.compile(r"^\w+$")

class ContactMessageForm(ModelForm):
	class Meta:
		model = models.ContactMessage
		fields = ['sendername', 'senderemail', 'message']
