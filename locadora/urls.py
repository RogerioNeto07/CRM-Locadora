"""
URL configuration for locadora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>', views.Details.as_view(), name='details'),
    path('adicionar', views.Create.as_view(), name='adicionar'),
    path('registrarpedido', views.RegistarPedido.as_view(), name='registrarpedido'),
    path('pedidos', views.Pedidos.as_view(), name='pedidos'),
    path('jogo/editar/<int:pk>/', views.EditarJogo.as_view(), name='editar_jogo'),
    path('jogo/deletar/<int:pk>/', views.DeletarJogo.as_view(), name='deletar_jogo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
