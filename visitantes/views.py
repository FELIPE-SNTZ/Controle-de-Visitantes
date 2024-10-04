from django.shortcuts import  get_object_or_404, render, redirect
from visitantes.forms import AutorizaVisitanteForm, VisitanteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from visitantes.models import Visitante


# Create your views here.

@login_required
def registrar_visitante(request):
    form = VisitanteForm()

    if request.method == 'POST':
       form = VisitanteForm(request.POST)

       if form.is_valid():
         visitante = form.save(commit=False)

         visitante.registrado_por = request.user.porteiro
         visitante = form.save()

         messages.success(request,'Visitante registrado com sucesso')
         return redirect('index')
       
    context = {
        'nome_pagina': 'Registrar visitante',
        'form': form
        }    

    return render(request,'registrar_visitante.html',context)


@login_required
def informacoes_visitante(request,pk):
    visitante = get_object_or_404(Visitante,pk=pk)

    # form = AutorizaVisitanteForm
    # if request.method == 'POST':
    #     form = AutorizaVisitanteForm(
    #        request.POST,
    #        instance=visitante
    #     )
    #     if form.is_valid():
    #        visitante = form.save()
    #        Visitante = form

    context = {
        'nome_pagina': 'Informações Visitante',
        'visitante': visitante
    }
    return render(request,'informacoes_visitante.html',context)



   