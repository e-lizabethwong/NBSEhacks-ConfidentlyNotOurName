from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from image_upload.models import ImageUpload
from django.conf import settings
from cohereChat import cohereChat
from image_upload.forms import ImageUploadForm

def home(request):
    myimages = ImageUpload.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'myimages': myimages,
    }
    return HttpResponse(template.render(context, request))

def personal(request):
    return render(request, 'personal.html')

def map(request):
    return render(request, 'map.html')

def chatbot(request, mentor_name, work_field):  # Add mentor_name here
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == "POST":
        user_message = request.POST.get('user_message', '')
        bot_response = cohereChat(user_message, work_field)
        request.session['chat_history'].append(('User', 'me', user_message))
        # Use my_string instead of 'Bot'
        request.session['chat_history'].append((mentor_name, work_field, bot_response))
        request.session.modified = True
        return redirect('chatbot', mentor_name=mentor_name, work_field=work_field)  # Pass my_string back to maintain it across requests

    chat_history = request.session['chat_history']
    return render(request, 'chatbot.html', {'chat_history': chat_history, 'mentor_name': mentor_name, 'work_field': work_field})

def end_chat_session(request):
    # Clear chat history from the session
    if 'chat_history' in request.session:
        del request.session['chat_history']
    # Redirect to the personal page
    return redirect('personal')  # Ensure you have a URL named 'personal'

def map_search(request):
    query = request.GET.get('q', '')
    # Here you'd typically perform the search on your models based on the query
    # For example, if searching in a model called 'Product':
    # results = Product.objects.filter(name__icontains=query)
    results = []  # Replace with actual search logic
    return render(request, 'map_search.html', {'query': query})

def asset(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ImageUploadForm()
    return render(request, 'asset.html', {'form': form})