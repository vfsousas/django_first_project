from django.conf.urls import url
from  myFirstApp import views

urlpatterns = [
    url(r'$', views.index, name='index')
]

