from django.shortcuts import render

# Create your views here.

def user_login_view(request):
	template_name = 'login.html'
	return render(request, template_name, {})


def user_register_view(request):
	template_name = 'register.html'
	return render(request, template_name, {})


def user_logout_view(request):
	template_name = 'logout.html'
	return render(request, template_name, {})