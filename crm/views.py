from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
import requests


def login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin:index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff and user.is_active:
                auth_login(request, user)
                return redirect('admin:index')
            else:
                return render(request, 'login.html', {'message': 'You are not authorized to access this admin site.'})
        else:
            return render(request, 'login.html', {'message': 'Oops, that username and password combination did not '
                                                             'work!'})
    return render(request, 'login.html')


def quick_add_customer(request):
    pass


def create_customer():

    payload = {
        "customer": {
            "first_name": "Naruto",
            "last_name": "Erh Kim Joo",
            "email": "narutokimjoo@alexandr.co",
            "phone": "+6598767898",
            "verified_email": True,
            "addresses": [],
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    r = requests.post(
        "https://07f482e43a73c9a534d365cddd9e7603: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@chrysalis-silk"
                      "-treasures.myshopify.com/admin/api/2021-04/customers.json",
        json=payload,
        headers=headers
    )
    print(r.json())


