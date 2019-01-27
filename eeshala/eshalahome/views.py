from django.shortcuts import render
from .models import pdfs, ContactMessage
from .forms import ContactMessageForm
from django.views.generic.edit import FormView, CreateView

# Create your views here.

def homeview(request):
	return render(request, 'index.html')


def listpdf(request):
	"""
	show the list of the pdfs

	"""

	pdflist = pdfs.objects.all().order_by('-pk');
	pkey = []
	title = []
	urls = []
	for i in pdflist:
		pkey.append(i.pk);
		title.append(i.title);
		filename = i.file.name
		k = filename.find("/")
		filename = filename[k::]
		urls.append(filename)


	pdfdetaillist = zip(pkey, title, urls)
	return render(request, 'pdflist.html', {'pdfdetaillist' : pdfdetaillist})


def detailpdf(request, pk):
	"""
	show the detail of the pdf
	"""
	pdf = pdfs.objects.filter(pk_exact=pk)

	pdffile = pdf.file
	pdftitle = pdf.title

	return render(request, 'renderpdf.html', {'pdffile':pdffile, 'pdftitle': pdftitle})


def appsview(request):
	return render(request, 'apps.html')

def videoview(request):
	return render(request, 'videos.html')

def contactview(request):
	return render(request, 'contact.html')


# view for contact form 
class ContactMessageCreate(CreateView):
    template_name = "ContactMessage_create_form.html"
    form_class = ContactMessageForm
    success_url = '/contacted/'
    model = ContactMessage
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ContactMessageCreate, self).form_valid(form)
