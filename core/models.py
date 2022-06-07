from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # no máximo 100 caracteres
    descricao = models.TextField(blank=True, null=True) # pode ficar em branco e ser nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) # Inseri a hora atual automaticamente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # se o usuario for deletado, seu evento tambem será deletado

    class Meta:
        db_table = 'evento' # exige que a tabela chaemo 'evento'

    def __str__(self):
        return self.titulo

    # Função para melhorar a exibição das datas e horas
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')