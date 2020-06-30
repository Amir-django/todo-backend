from django.contrib import admin
from django.urls import path,include
from qwerty import views

urlpatterns = [
    path('', views.index,name="list"),
    path('update_task/<str:pk>', views.update_task, name="update_task"),
    path('delete/<str:pk>',views.delete,name="delete")
]