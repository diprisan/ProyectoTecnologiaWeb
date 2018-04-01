from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('indice/', views.indice, name='indice'),
	# ex: /polls/5/results/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
	path('indexRender/', views.indexRender, name='indexRender'),
	path('<int:question_id>/detalle/', views.detailsExcep, name='detailsExcep'),
    path('home/', views.home, name='home'),
    path('detailsLogin/<user_id>/<pass_id>/', views.detailsLogin,  name='detailsLogin'),
	path('detailsExcep/<int:question_id>', views.detailsExcep,  name='detailsExcep'),
    path('login2/', views.login2, name='login2'),
]