from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from image_upload.models import ImageUpload

def home(request):
    myimages = ImageUpload.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'myimages': myimages,
    }
    return HttpResponse(template.render(context, request))