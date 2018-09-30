from django.urls import path
from . import views

urlpatterns=[
	path('', views.index),
	path('<int:page>/', views.index),
	path('<str:slug>/', views.product_views, name='product'),
]