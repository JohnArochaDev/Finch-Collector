from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch_index, name='index'),
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
]