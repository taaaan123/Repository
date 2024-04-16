from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/new/', views.car_create, name='car_create'),
    path('car/<int:pk>/edit/', views.car_update, name='car_update'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('show/<str:color>/', views.show_car, name='show_car'),
    path('car/<int:pk>/<str:type>/<str:color>/', views.swap_cars, name='swap_cars'),

]
