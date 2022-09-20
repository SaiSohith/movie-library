# from curses.ascii import HT
import json
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

# def index(request):
#     # return HttpResponse('Hellow')
#     return render(request,'register.html')

def home(request):
    return render(request,'home.html')


def movies(request):
    res={'Search':[]}
    if request.method == 'POST':
        query = request.POST['restname']
        res=requests.get(f'https://www.omdbapi.com/?s={query}&apikey=ab0b8847').json()
        print(res)
        # return HttpResponse(json.dumps(res))
        # return render(request,'home.html',{'res':query})
    return render(request,'home.html',{'res':res['Search']})


# def register(request):
#     if request.method=='POST':
#         username=request.POST['user_name']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         email=request.POST['email']
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 print('User name already Exists')
#                 return render(request, 'registration.html', {'errormsg': 'User name already Exists'})
#             elif User.objects.filter(email=email).exists():
#                 print('Account based on email already exists')
#                 return render(request, 'registration.html', {'errormsg': 'email already Exists'})
#             else:
#                 user=User.objects.create_user(username=username,password=password1,email=email)
#                 user.save()
#                 print('user created')
#                 return render(request, 'registration.html', {'errormsg': 'Sign Up Completed'})
#         else:
#             print('password not matching')
#             return render(request, 'registration.html', {'errormsg': 'Password Not Matched'})
#     else:
#         return render(request,'registration.html')



# def loginuser(request):
#     if request.method == 'POST':
#         uname = request.POST['uname']
#         passw = request.POST['pass']
#         msg = "invalid credentials"
#         try:
#             user = auth.authenticate(request, username=uname, password=passw)
#             print(user)
#         except:
#             print('in exxcept')
#             return render(request, 'login.html', {'msg': msg})
#         if user is not None:
#             print('authenticated')
#             auth.login(request, user)
#             return render(request, 'home.html')
#     return render(request, 'login.html')


# def logoutuser(request):
#     auth.logout(request)
#     return redirect('/')

