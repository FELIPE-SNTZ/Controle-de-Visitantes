from django.shortcuts import render

# Create your views here.



def morador(request):
    
    return render(request, 'morador.html')