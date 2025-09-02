from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jogos', views.JogoViewSet)
router.register(r'DLCs', views.DLCViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'generos', views.GeneroViewSet)
router.register(r'plataformas', views.PlataformaViewSet)
router.register(r'pedidos', views.PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('faturamento/', views.FaturamentoView.as_view(), name='faturamento'),
]