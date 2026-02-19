from django.urls import path
from . import views

app_name = 'divisions'

urlpatterns = [
    path('', views.division_list, name='division_list'),
]