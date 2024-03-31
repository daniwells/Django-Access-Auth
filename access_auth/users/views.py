from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Already exists a user with this username')
        
        user = User.objects.create_user(username=username,  email=email, password=password)
        user.save() 

        return HttpResponse('User registerd with successfuly')
    return render(request, "register.html")
    

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("Authenticated!!")
        return HttpResponse("username or password invalidaded!!")        
    return render(request, 'login.html')

@login_required
def plataform(request):
    # if request.user.is_authenticated:
    #     return HttpResponse('Plataform')
    # return HttpResponse('Do you need is loged for access this page!!')

    return HttpResponse('Plataform')