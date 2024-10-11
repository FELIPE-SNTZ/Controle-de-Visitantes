from django.db import models

# Create your models here.
class Morador(models.Model):

    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=200)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', auto_now= False, auto_now_add=False)
    telefone = models.CharField(verbose_name='Telefone', max_length=11)
    numero_casa = models.PositiveSmallIntegerField(verbose_name='Número do Apartamento')


    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]

            cpf_formatado = f'{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}'
            return cpf_formatado
        
    class Meta:
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"
        db_table ='morador'

    def __str__(self):
        return self.nome_completo

