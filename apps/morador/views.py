from django.shortcuts import get_object_or_404, render

from morador.models import Morador

# Create your views here.
def informacoes_morador(request,pk):
    morador = get_object_or_404(Morador,pk=pk)
    context = {
        'nome_pagina': 'Informações Morador',
        'morador': morador,
    }
    return render(request,'informacoes_morador.html',context)

    


def morador(request):
    morador = Morador.objects.order_by('nome_completo')
    
    return render(request, 'morador.html',{'morador':morador})