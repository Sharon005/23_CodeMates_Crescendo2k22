from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from .models import *

from Animal_Rescue_Portal import settings

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib import messages

import requests

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Web_App:signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Web_App:signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Web_App:signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Web_App:signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Web_App:signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to Animal Rescue Portal Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Animal Rescue Portal!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n Animal Rescue Team"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Animal Rescue Portal Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('Web_App:signin')
        
        
    return render(request, "Web_App/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('Web_App:signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "Web_App/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('Web_App:signin')
    
    return render(request, "Web_App/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Web_App:signin') 

def home(request):
    return render(request, 'Web_App/index.html')

def adoption(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        age = request.POST.get('age')        
        email = request.POST.get('email')
        message = request.POST.get('message')
        number = request.POST.get('number')
        image = request.POST.get('image')

        adoption = ContactUS(name=name, gender=gender, category=category, age=age, email=email,   number=number, message=message, image=image,) 

        adoption.save()
        messages.success(request, 'Your form has been submitted!')
    return render(request, 'Web_App/adoption.html')

def contact(request):
    return render(request, 'Web_App/contact.html')

def about(request):
    return render(request, 'Web_App/about.html')

