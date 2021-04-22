from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
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
