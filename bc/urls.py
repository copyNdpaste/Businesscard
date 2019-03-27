from django.urls import path, include
from bc import views

urlpatterns = [
    path('create/', views.create),
    path('list/', views.list),
    path('list/update/', views.update),
    path('list/delete/', views.delete),
    path('list/search/', views.search),
]