from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'Web_App'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),    
    path('signout', views.signout, name='signout'),
    path('home', views.home, name="home"),
  
    
]
