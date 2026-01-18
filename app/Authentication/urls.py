from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Home, name = 'Home'),
    path('', views.LoginView, name = 'Login'),
    path('register/', views.RegisterView, name = 'Register'),
    path('logout/', views.LogoutView, name = 'Logout'),
    path('forgot-password/', views.ForgotPassword, name = 'forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name = 'password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name = 'reset-password'),
    path('profile/<str:username>/', views.ProfileView, name = 'Profile'),
]
