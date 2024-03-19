
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    #crud
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-record', views.add_record, name="add-record"),
    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('record/<int:pk>', views.single_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),





]