from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criando_django/', views.criando_django, name='criando_django'),
    path('fundamentos_csharp/', views.fundamentos_csharp, name='fundamentos_csharp'),
    path('fundamentos_python/', views.fundamentos_python, name='fundamentos_python'),
    path('fundamentos_flutter/', views.fundamentos_flutter, name='fundamentos_flutter'),
]