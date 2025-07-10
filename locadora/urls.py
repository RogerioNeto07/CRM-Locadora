from django.contrib import admin
from django.urls import path, include
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
    path('api/', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
