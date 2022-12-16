from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from rest_framework.viewsets import ModelViewSet
from .models import Document
from .Predicter import summarize
from PyPDF2 import PdfReader

import os


def index(request):
    return render(request, 'apiv1.html')


def save_file(title: str, abstract: str, pdf_file) -> bool:
    if title == "" or abstract == "" or pdf_file is None:
        return False

    if not os.path.exists("PDF_FILES"):
        os.mkdir("PDF_FILES")

    fs = FileSystemStorage()
    filename: str = "PDF_FILES/" + pdf_file.name
    fs.save(filename, pdf_file)
    try:
        d = Document(title, filename, abstract)
        d.save()
    except:
        return False
    return True


def cache_pdf(pdf_file) -> str:
    if not pdf_file or pdf_file == None:
        return ""
    if not os.path.exists("CACHE"):
        os.mkdir("CACHE")

    fs = FileSystemStorage()
    filename: str = "CACHE/" + pdf_file.name
    fs.save(filename, pdf_file)
    return filename


def document(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        return JsonResponse({'documents': list(documents.values())})
    elif request.method == 'POST':
        pdf = request.FILES['PDF']
        title = request.POST["Title"]
        abstract = request.POST["Abstract"]
        save_file(title, abstract, pdf)
        return HttpResponse('')


def document_detail(request, pk):
    if request.method == 'GET':
        pdf = Document.objects.get(pk=pk)
        return JsonResponse({'document': pdf})

    elif request.method == 'POST':
        pdf = request.FILES['PDF']
        abstract = request.POST["Abstract"]
        save_file(pk, abstract, pdf)
        return HttpResponse('')

    elif request.method == 'DELETE':
        doc = Document.objects.get(pk=pk)
        os.remove(doc.location)
        return HttpResponse('')



def train(request):
    pdf = request.FILES['PDF']
    return JsonResponse({'abstract': 'This is the abstract of the PDF file'})


def predict(request):
    pdf = request.FILES['file']
    filename = cache_pdf(pdf)

    if filename != "":
        # read the pdf file
        reader = PdfReader(filename)
        text: str = ""
        for page in reader.pages:
            text += page.extractText()
        # summarize the text
        abstract = summarize(text, 0.1)

        # delete the cached file
        os.remove(filename)
        return JsonResponse({
                'Success': True,
                'Abstract': abstract
            })
    else:
        return JsonResponse({
                'Success': False,
            })



def document_view(request):
    context = {
        'documents': Document.objects.all()
    }
    return render(request, 'document_view.html', context)


def document_detail_view(request, title):
    context = {
        'document': Document.objects.get(pk=title)
    }
    return render(request, 'document_detail_view.html', context)

