from django.shortcuts import render,redirect





from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

from .models import Contact

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            subject = f"New contact form submission from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    email,  # From email
                    ['vaivaideesh33@gmail.com'],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Message sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'Failed to send message: {e}')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'index.html')
