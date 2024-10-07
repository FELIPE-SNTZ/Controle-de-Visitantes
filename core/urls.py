from apps.visitantes.views import finalizar_visita
from apps.dashboard.views import index
from django.contrib import admin
from django.urls import path
from apps.visitantes.views import registrar_visitante, informacoes_visitante
from django.contrib.auth import views as auth_views
from apps.visitantes.views import informacoes_visitante


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registro',registrar_visitante,name='registrar_visitante'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('visitante/<int:pk>', informacoes_visitante,name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita', finalizar_visita,name='finalizar_visita')


]
