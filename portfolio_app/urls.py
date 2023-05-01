from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact'),
]
