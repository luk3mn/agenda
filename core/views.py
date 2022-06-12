from email import message
from django.shortcuts import redirect, render
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