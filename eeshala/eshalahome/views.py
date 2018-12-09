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
	for i in pdflist:
		pkey.append(i.pk);
		title.append(i.title);

	pdfdetaillist = zip(pkey, title)
	return render(request, 'pdflist.html', {'pdfdetaillist' : pdfdetaillist})


def detailpdf(request, pk):
	"""
	show the detail of the pdf
	"""
	pdf = pdfs.objects.filter(pk_exact=pk)

	pdffile = pdf.file
	pdftitle = pdf.title

	return render(request, 'renderpdf.html', {'pdffile':pdffile, 'pdftitle': pdftitle})
