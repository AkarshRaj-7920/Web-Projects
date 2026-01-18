from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('new/', views.CreatePostView, name = 'post-create'),
    path('<int:pk>/delete/', views.DeletePostView, name = 'post-delete'),
    path('<int:pk>/post-detail/', views.PostView, name = 'post-detail'),
]

