from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
