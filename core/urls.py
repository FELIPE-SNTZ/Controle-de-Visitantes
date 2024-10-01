from dashboard.views import index
from django.contrib import admin
from django.urls import path
from visitantes.views import registrar_visitante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('registro',registrar_visitante,name='registrar_visitante')

]
