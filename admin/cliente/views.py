from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from .forms import NameForm

# Create your views here.
def show(request):
	return HttpResponse("Hola desde el cliente")

def marcadores(request):
	return render (request, 'marcadores.html', {})
	
def login(request):
	if request.method == 'POST'	:
		username = request.POST['username']
		password = request.POST['password']
		print (username)
		print (password)
	form = LoginForm()
	context = { 'from' : form, }
	return render (request, 'login.html', {'form': form})
	
def name(request): 
	form = NameForm()
	return render(request, 'name.html', {'form': form})