from apps.dashboard.views import index
from django.contrib import admin
from django.urls import path, include
from apps.visitantes.views import registrar_visitante, informacoes_visitante,finalizar_visita
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),

    
    path('login/',LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name = 'logout.html'), name='logout'),


    path('registro',registrar_visitante,name='registrar_visitante'),
    path('visitante/<int:pk>', informacoes_visitante,name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita', finalizar_visita,name='finalizar_visita'),


    path('api/',include('api.urls'))
    
]
