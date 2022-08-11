from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='account_login'),
    path('accounts/login/', views.LoginView.as_view(), name='account_signup'),
    path('update/<int:pk>/', views.UpdateStateView.as_view(), name='update'),
]   
