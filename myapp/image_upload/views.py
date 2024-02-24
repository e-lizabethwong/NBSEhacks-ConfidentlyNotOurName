from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form': form})