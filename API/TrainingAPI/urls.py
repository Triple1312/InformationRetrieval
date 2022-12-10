from django.urls import path
from django.conf.urls import include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('document', document, name='document'),
    path('document/<int:pk>', document_detail, name='document_detail'),
    path('train', train, name='train'),
    path('document_view', document_view, name='document_view'),
    path('document_view/<str:title>', document_detail_view, name='document_detail_view'),
]