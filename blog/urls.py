from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blogHome, name='home'),
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    
]