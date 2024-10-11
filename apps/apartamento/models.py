from django.db import models

# Create your models here.
class Apartamento(models.Model):

    vagas = models.CharField(verbose_name='Vagas de Estacionamento',max_length=2)
    bloco = models.CharField(verbose_name='Bloco', max_length=1)
    numero = models.PositiveSmallIntegerField(verbose_name='Número do Apartamento')


    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"
        db_table ='apartamento'

    def __str__(self):
        return self.numero