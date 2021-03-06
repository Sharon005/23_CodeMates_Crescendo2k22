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
<<<<<<< HEAD
    path('volunteer', views.volunteer, name="volunteer"),
    
    path('donate', views.donate, name="donate"),
    path('success', views.success, name="success"),

=======
    path('register', views.register, name="register"),
>>>>>>> 46c88e96d00d51822270b937efc35f009bb0999d

    url(r'^animals/$', views.AnimalDView.as_view(), name='animal'),
    url(r'^animals/(?P<slug>[A-Za-z0-9_-]+)/$', views.AnimalView.as_view(), name='animal_desc'),
    
]
