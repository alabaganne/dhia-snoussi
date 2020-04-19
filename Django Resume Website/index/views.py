from django.shortcuts import render
from .models import Message

from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Message(name=name, email=email, subject=subject, message=message).save()
        return HttpResponse('Your message has been submitted. Thanks!')

    else:
        return render(request, 'index.html')