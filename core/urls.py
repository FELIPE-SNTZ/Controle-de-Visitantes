from apps.apartamento.views import apartamento
from apps.dashboard.views import index
from django.contrib import admin
from django.urls import path, include
from apps.visitantes.views import registrar_visitante, informacoes_visitante,finalizar_visita
from apps.morador.views import morador,informacoes_morador
from django.contrib.auth.views import LoginView,LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('morador/',morador,name='morador'),
    path('informacoes_morador/<int:pk>', informacoes_morador,name='informacoes_morador'),
    path('apartamento/',apartamento,name='apartamento'),

    
    

    path('login/',LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name = 'logout.html'), name='logout'),


    path('registro',registrar_visitante,name='registrar_visitante'),
    path('visitante/<int:pk>', informacoes_visitante,name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita', finalizar_visita,name='finalizar_visita'),

    path('api/',include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
