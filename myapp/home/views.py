from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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

def map(request):
    return render(request, 'map.html')

def chatbot(request, mentor_name):  # Add mentor_name here
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == "POST":
        user_message = request.POST.get('user_message', '')
        bot_response = f"Echo: {user_message}"
        request.session['chat_history'].append(('User', user_message))
        # Use my_string instead of 'Bot'
        request.session['chat_history'].append((mentor_name, bot_response))
        request.session.modified = True
        return redirect('chatbot', mentor_name=mentor_name)  # Pass my_string back to maintain it across requests

    chat_history = request.session['chat_history']
    return render(request, 'chatbot.html', {'chat_history': chat_history, 'mentor_name': mentor_name})

def end_chat_session(request):
    # Clear chat history from the session
    if 'chat_history' in request.session:
        del request.session['chat_history']
    # Redirect to the personal page
    return redirect('personal')  # Ensure you have a URL named 'personal'