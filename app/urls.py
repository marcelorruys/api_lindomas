from django.urls import path, include

from app.views import listar_clientes, ClientesView

urlpatterns = [
    path('clientes', listar_clientes),
    path('usuarios', ClientesView.as_view()),
    path('usuarios/<int:pk>', ClientesView.as_view()),
]
