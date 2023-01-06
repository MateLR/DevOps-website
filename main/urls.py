from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Demand', views.stat, name='demand'),
    path('Geography', views.stat, name='geo'),
    path('Skills', views.stat, name='skills'),
    path('Last-vacancies', views.stat, name='last-vacs')
]
