from django.urls import path, include
from bc import views

app_name = 'bc'
urlpatterns = [
    path('create/', views.create),
    path('list/', views.list, name='list'),
    path('list/update/', views.update),
    path('list/delete/', views.delete),
    path('list/search/', views.search),
]