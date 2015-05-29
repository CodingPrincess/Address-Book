from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from book.models import PhoneNumber, Email_Add, Pin, SocialNetwork, Website
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.db import IntegrityError
from django import forms
import random, string

# Create your views here.

def index(request):
    return render(request, 'book/index.html')
        
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('/book/login/')

        else:
            return HttpResponse("Your username and password didn't match.")

    else:
        return render(request, 'book/login.html',{})
    
def signout(request):                                     # Logout the user
    logout(request)
    return HttpRequestRedirect('/book/')

def profile_user(request):
    return render(request, 'book/userprofile.html')

def edit_profile(request):

    if request.method == 'POST':
        phone_num = request.POST['phone']
        email_id = request.POST['email']
        website = request.POST['website']
        blog = request.POST['blog']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        ph = Phone.objects.create(phone = phone_num, user_id = request.user.id)
        mid = MailAddress.objects.create(email_address = email_id, user_id = request.user.id)
        web = WebDetail.objects.create(web_site = website, blog = blog, user_id = request.user.id)
        info = Information.objects.create(facebook = facebook, twitter = twitter, user_id = request.user.id)
        return HttpResponse("Successful")

    else:
        return render(request, 'book/edit.html', {})

def signup(request):                                      # For new user
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            registered = True
            return HttpResponseRedirect('/book/userprofile/')
    else:
        user_form = UserCreationForm()

    return render(request, 'book/register.html', {
        'user_form' : user_form, 'registered' : registered
        })

def gen_random(request):
    rpin = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
    pp = Pin.objects.create(user_pin = rpin, user_id = request.user.id)
    return render(request, 'book/generate_pin.html', {})


def pub_profile(request, user_id):
    try:
        user = User.objects.get(pk = user_id)
    except User.DoesNotExist:
        raise Http404("Invalid username!!")
    return render(request, 'book/publicProfile.html', {'user':user})


def user_contacts(request):
    con = get_object_or_404(User, pk = request.user.id)
    return render(request, 'book/mycontacts.html', {'con' : con})


