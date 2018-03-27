from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^show/$', views.show ),
	url(r'^login/$', views.login ),
	url(r'^marcadores/$', views.marcadores ),
	url(r'^name/$', views.name ),

]

