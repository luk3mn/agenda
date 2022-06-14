from email import message
import re
from django.shortcuts import redirect, render
from pkg_resources import require
from requests import request
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Redireciona o usuario para a página de login
def login_user(request):
    return render(request, 'login.html')

# Para fazer o logout do usuário
def logout_user(request):
    logout(request) # vai limpar a sessão
    return redirect('/') # redireciona para o index

# Para fazer a autenticação do usuario pelo formulario
def submit_login(request):
    if request.POST: # se o método de requisição for POST
        # armazena na variável 'username' o username vindo do formulario através do método POST
        username = request.POST.get('username')
        # armazena na variável 'password' o password vindo do formulario através do método POST
        password = request.POST.get('password')

        # autentica o usuário
        usuario = authenticate(username=username, password=password)
        if usuario is not None: # teste sé não é vazio
            login(request, usuario) # faz o login
            return redirect('/') # redireciona pro index
        else: # se ele não consegui autenticar vai cair nesse erro
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/') # redireciona para a página principal, como não estará logado ele será mandado para a página de login

# para identificar que é um decorador -> requer o login para acessar a lista
@login_required(login_url='/login/') # [login_url='/login/'] => Significa que quando ele não estiver logado, será redirecionado para a página de login
# Funçõa que vai renderiar a página HTML
def lista_eventos(request):
    usuario = request.user # pega o usuário que está enviando a requisição
    evento = Evento.objects.filter(usuario=usuario) # Mesma coisa do 'all' porém está sendo passado um filtro
    # evento = Evento.objects.get(id=1) # pega apenas um registro do banco
    # evento = Evento.objects.all() # pega todos os registros do banco
    dados = {'eventos':evento} # dicionario
    return render(request, 'agenda.html', dados) # renderiza o template HTML criado

# função para redirecionar a página inicial para o index
# def index(request):
#     return redirect('/agenda/')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento: # se tiver o id_evento
        # passa o evento
        dados['evento'] = Evento.objects.get(id=id_evento) 
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo') # recebe o titulo do form pelo metodo POST
        data_evento = request.POST.get('data_evento') # recebe a data do evento do form pelo metodo POST
        descricao = request.POST.get('descricao') # recebe a descricao do form pelo metodo POST
        usuario = request.user # pega o usuario que está criando o evento
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            # Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                    #    data_evento=data_evento,
                                                    #    descricao=descricao)
        else:
            # Inseri os dados do evnto no banco de dados a partir do Models do app 'core'
            Evento.objects.create(titulo=titulo,
                                data_evento=data_evento,
                                descricao=descricao,
                                usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/') # tem que está logado
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento) # pega pelo 'id'
    if usuario == evento.usuario: # valida se o evento pertemce ao usuário logado
        evento.delete() # aplica a exclusão com o 'delete()
    return redirect('/') # redireciona para a página principal
