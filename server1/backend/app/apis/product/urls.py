from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('items/', views.ItemListCreateView.as_view(), name='item-list-create'),
]