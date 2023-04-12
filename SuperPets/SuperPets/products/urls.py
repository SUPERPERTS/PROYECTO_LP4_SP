from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

products_patterns = ([ # Cambiando nombre de urlpatterns y generando un tupla de las urls y agregando un segundo elemnto llamado 'Products'
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

], 'products')