from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from shop.models import ShopModel, ShopOwner
from route.models import RouteModel

# Create your views here.


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('Login')

        else:
            login(request,user)
            # messages.success(request, "You have successfully signed in")
            return redirect('Index')
        
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request, "You have successfully signed out")
    return redirect('Login')



def Index(request):
    routesCounts = RouteModel.objects.all().count()

    shopsCounts = ShopModel.objects.all().count()

    shopsOwnersCounts = ShopOwner.objects.all().count()

    return render(request, 'index.html', context={'routesCounts': routesCounts, 'shopsCounts':shopsCounts, 'shopsOwnersCounts': shopsOwnersCounts})

