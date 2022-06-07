from django.shortcuts import redirect, render
from core.models import Evento

# Create your views here.

# Funçõa que vai renderiar a página HTML
def lista_eventos(request):
    # usuario = request.user # pega o usuário que está enviando a requisição
    # evento = Evento.objects.filter(usuario=usuario) # Mesma coisa do 'all' porém está sendo passado um filtro
    # evento = Evento.objects.get(id=1) # pega apenas um registro do banco
    evento = Evento.objects.all() # pega todos os registros do banco
    dados = {'eventos':evento} # dicionario
    return render(request, 'agenda.html', dados) # renderiza o template HTML criado

# função para redirecionar a página inicial para o index
# def index(request):
#     return redirect('/agenda/')