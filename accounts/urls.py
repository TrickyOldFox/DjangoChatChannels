from django.contrib.auth import views
from django.urls import path
from . import views as vs

urlpatterns = [
    path('', vs.home, name='home'),
    path('login/', vs.login, name='accounts_login'),
    path('logout/', vs.logout, name='logout'),
    path('register/', vs.register, name='register'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', vs.login, name='password_change_done'),
]