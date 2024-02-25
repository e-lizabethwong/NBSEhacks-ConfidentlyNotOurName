from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from image_upload.models import ImageUpload
from django.conf import settings

def home(request):
    myimages = ImageUpload.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'myimages': myimages,
    }
    return HttpResponse(template.render(context, request))

def personal(request):
    return render(request, 'personal.html')