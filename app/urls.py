from django.urls import path
from app import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings   

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('restock/<int:pk>/', views.RestockView.as_view(), name='restock'),
    path('addlist/<int:pk>/', views.AddListView.as_view(), name='addlist'),
    path('additem/', views.AddItemView.as_view(), name='additem'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)