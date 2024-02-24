from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def image_upload(request):
    return HttpResponse("Hello world!")