from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registro', views.registro, name='registro'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
]