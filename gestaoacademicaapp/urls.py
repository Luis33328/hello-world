from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login.html', views.login, name='login'),
    path('esq_senha.html', views.esq, name='esq_senha'),
    path('home.html', views.home, name='home'),
    path('index.html', views.listaMatriculas, name='lista-disciplinamatricula'),
    path('fazerMatricula/<int:id>', views.fazerMatricula, name="alterar-statusmatricula"),

]
