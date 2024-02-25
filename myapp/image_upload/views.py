from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm
from .models import ImageUpload

# def image_upload_view(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'image_upload.html', {'form': form})

def asset(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save()
            # Redirect to a new URL to display the image
            return redirect('analyzer', image_id=image_upload.id)
    else:
        form = ImageUploadForm()
    return render(request, 'asset.html', {'form': form})

def analyzer(request, image_id):
    # Retrieve the uploaded image by ID
    image_upload = ImageUpload.objects.get(id=image_id)
    return render(request, 'analyzer.html', {'image_upload': image_upload})

def main(request):
    return redirect('asset')