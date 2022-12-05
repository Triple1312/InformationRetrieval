from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import Document


def index(request):
    return render(request, 'apiv1.html')


def document(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        return JsonResponse({'documents': list(documents.values())})
    elif request.method == 'POST':
        pdf = request.FILES['file']
        print(pdf)


def document_detail(request, pk):
    if request.method == 'GET':
        pdf = Document.objects.get(pk=pk)
        return JsonResponse({'document': pdf})


def train(request):
    pass


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

