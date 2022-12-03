from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import Document


def index(request):
    return HttpResponse("Index")


def document(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        return JsonResponse({'documents': list(documents.values())})
    elif request.method == 'POST':
        pass



