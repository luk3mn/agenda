"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/<int:id_usuario>/', views.json_lista_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento), # cria uma rota o submit do form de evento
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento), # cria uma rota para exclusão de dados do dataset
    # path('', views.index) # uma forma de redirecionar a página inicial chamando uma view que nesse caso tem o nome de 'index' e a funcao index na view fará o redirecionamento da página
    path('', RedirectView.as_view(url='/agenda/')), # uma forma mais direta de redireciona a página inicial para um index
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user), # deslogar o usuario 
]
