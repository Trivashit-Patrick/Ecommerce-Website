from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup',views.handleSignup , name='handleSignup'),
    path('login',views.handleLogin , name='handleLogin'),
    path('logout',views.handleLogout , name='handleLogout'),
]