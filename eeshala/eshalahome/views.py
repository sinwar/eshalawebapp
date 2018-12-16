from django.shortcuts import render
from .models import pdfs

# Create your views here.

def homeview(request):
	return render(request, 'index.html')


def listpdf(request):
	"""
	show the list of the pdfs

	"""

	pdflist = pdfs.objects.all();
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
