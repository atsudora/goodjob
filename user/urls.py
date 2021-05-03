from django.urls import path
from . import views

appname = 'user'

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
]