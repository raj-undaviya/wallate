from django.shortcuts import render, redirect
from .models import *
import string, random
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def register(request):
    if request.method == 'POST':
        randomstr = ''.join(random.choices(string.digits, k=5))
        user_id = 'BIN' + randomstr
        first_name =  request.POST.get('first_name')
        last_name =  request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        encrypted_password = make_password(password)
        profile_image = request.FILES.get('profileimg')
        print(profile_image)
        if user_profile.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'User already registered.'})
        else:
            userdata = user_profile(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=encrypted_password,
                profile_image=profile_image
            )
            userdata.save()
            response = redirect('homePage')
            return response
    return render(request, 'register.html')

def dashboard(request):
    userdata = request.session.get('userdata')
    
    return render(request, 'dashboard.html', {'userdata':userdata})

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = user_profile.objects.get(username=username)
        if username == user.username:
            if check_password(password, user.password):
                session_data = {
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email
                }
                request.session['userdata'] = session_data
                return redirect('dashbaordPage')
            else:
                print("INVALID PASSWORD......................")
                return redirect('homePage')
        else:
            print("USERNAME IS NOT EXSISTS.....")
            return redirect('homePage')
    return render(request, 'index.html')