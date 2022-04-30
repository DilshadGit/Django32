from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def user_login_view(request):
    # future -> ?next=/articles/crete
    template_name = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, template_name, context)

# def user_login_view_v1(request):
#     template_name = 'login.html'
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             context = {
#                 'error': 'Invalid username or password'
#             }
#             return render(request, template_name, context)
#         print(user)
#         login(request, user)
#         return redirect('/')
#     else:
#         form = AuthenticationForm(request)
#     # context = {
#     #     'username': username,
#     #     'password': password
#     # }
#     return render(request, template_name, {})


def user_register_view(request):
    template_name = 'register.html'
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        reg_form = form.save()
        return redirect('accounts:login')
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def user_logout_view(request):
    template_name = 'logout.html'
    if request.method == 'POST':
    	logout(request)
    	return redirect('accounts:login')
    return render(request, template_name, {})
