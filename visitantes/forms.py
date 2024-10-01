from django import forms
from .models import Visitante
from typing_extensions import Required


class VisitanteForm(forms.ModelForm):


    class Meta:
        model = Visitante
        fields = ['nome_completo','cpf','data_nascimento','numero_casa ','placa_veiculo']

        error_messages ={
            'nome_completo':{'required':'O nome completo do vistante é obrigatorio para o registro'},
            'cpf':{'required':'O CPF do vistante é obrigatorio para o registro'},
            'data_nascimento':{'required':'Por Favor,informe um formato valido para a data de nascimento (DD/MM/AAAA)'},
            'numero_casa ':{'required':'Por Favor,informe o número da casa a ser visitada'},
            
        }

class AutorizaVisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields =['morador_responsavel']

        
        error_messages ={
            'morador_responsavel':{'required':'Por Favor,informe o nome do morador responsavel por autorizar a entrada da visita'},}