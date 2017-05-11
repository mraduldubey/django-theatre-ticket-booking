from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render

# Create your views here.
def home(request):
	"""the homepage view"""
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	"""about page"""
	context = {}
	template = 'about.html'
	return render(request,template,context)

@login_required
def dashboard(request):
	"""about page"""
	context = {'user':request.user}
	template = 'dashboard.html'
	return render(request,template,context)
