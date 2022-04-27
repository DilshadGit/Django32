from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.


def user_login_view(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': 'Invalid username or password'
            }
            return render(request, template_name, context)
        print(user)
        login(request, user)
        return redirect('/admin')
    # context = {
    #     'username': username,
    #     'password': password
    # }
    return render(request, template_name, {})


def user_register_view(request):
    template_name = 'register.html'
    return render(request, template_name, {})


def user_logout_view(request):
    template_name = 'logout.html'
    if request.method == 'POST':
    	logout(request)
    	return redirect('/login/')
    return render(request, template_name, {})
