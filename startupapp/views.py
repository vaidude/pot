from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'index.html')