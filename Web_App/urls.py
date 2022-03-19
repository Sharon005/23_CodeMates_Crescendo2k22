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
    path('adoption', views.adoption, name="adoption"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),  

    url(r'^animals/$', views.AnimalDView.as_view(), name='animal'),
    url(r'^animals/(?P<slug>[A-Za-z0-9_-]+)/$', views.AnimalView.as_view(), name='animal_desc'),
    
]
