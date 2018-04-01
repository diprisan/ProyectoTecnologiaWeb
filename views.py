from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.template import Template , Context
from django.shortcuts import render_to_response
from django.template                import RequestContext

from .models import Usuarios
from .models import Question
import sys

def index(request):
    return HttpResponse("Hello, world. You're at twhe polls index.")
	
def results(request, question_id):
    response = "Tu pregunta es %s."
    return HttpResponse(response % question_id)

def indice(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse(" Tu ves la pregunta %s." % question_id)

def detailsExcep(request, question_id):
        queryId = Question.objects.get(id=question_id)
        return HttpResponse(queryId.question_text)
	
def indexRender(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    template = loader.get_template('polls/home.html')
    context = {
           }
    return HttpResponse(template.render(context, request))

def login2(request):
    template = loader.get_template('polls/login2.html')
    context = {
           }
    return HttpResponse(template.render(context, request))


def login(request):
    message = None
    if request.method == 'POST':
      username_post = request.POST['username']
      password_post = request.POST['password']
      user = authenticate ( username = username_post, password = password_post)
      if user is not None:
        login_django( request, user)
        #return redirect('polls:dashboard')
        return HttpResponseRedirect(reverse('polls:dashboard'))
      else:
        menssage = "incorrecto"
        #return redirect('polls:login')
        return HttpResponseRedirect(reverse('polls:login'))

      form = LoginForm()
      context = {
        'form' : form,
        'message' : message
      }
      return  render_to_response (request, 'polls/login.html',   {'form': form})
 


def dashboard(request):
   return render (request, 'polls/dashboard.html', {})
#, usuario, contra):

def loginGar(request, username=None):
    contra=""
    valor="";
    #queryId = Usuarios.objects.get(user=username, passw=contra)
    try:   queryId = Usuarios.objects.get(id=1)
    #template = loader.get_template('polls/home.html')
    #context = {   }
    #return HttpResponse(template.render(context, request))
    except DoesNotExist:
                valor="Hello, world. You're at twhe polls index."

def detailsLogin(request, user_id ,pass_id):
    valor="trae datos"
    try:     
        userId = Usuarios.objects.filter(user=user_id)
        userId = userId.filter(passw=pass_id)
        #return HttpResponseRedirect(reverse('polls:home'))
        #context = {'latest_question_list': userId}
        #return render(request, 'polls/index.html', context)
        if userId:
            context = {'latest_question_list': userId}
            return redirect('http://127.0.0.1:8000/polls/home/')

        else:
            valor="No hay registros con coindicencias"
    #print ("The answer is", 2*2) id=question_id,
    except Exception as e:
                valor="failed to: %s" % (str(e))
    return HttpResponse(valor)
                  
