from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == 'POST':
       
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = request.POST['subject']

        
                
        contact = Contact(name=name, email=email,
        phone=phone, message=message, subject=subject)

        contact.save()

        # Send email
        send_mail(
            'Company Inquiry',
            'There has been an inquiry for Enlighten/E.''From '+ name + ' Sign into the admin panel for more info',
            'johnny45gotu@gmail.com',
            ['johnny45gotu@outlook.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a rep will get back to you soon')
        return redirect('')  