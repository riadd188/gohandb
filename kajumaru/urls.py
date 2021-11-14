from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('update/<int:pk>/', views.UpdateStateView.as_view(), name='update'),

]   