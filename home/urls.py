from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('appointment.html', views.appointment, name='appointment'),
    path('contact.html', views.contact, name='contact'),
    path('open.html', views.open, name='open'),
    path('photo.html', views.photo, name='photo'),
    path('service.html', views.service, name='service'),
    path('team.html', views.team, name='team'),
    # path('testimonial.html', views.testimonial, name='testimonial'),
    path('video.html', views.video, name='video'),
]