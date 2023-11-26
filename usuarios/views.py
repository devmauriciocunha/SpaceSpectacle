from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)  # Puxa o formulário com os dados enviados pelo usuário

        if form.is_valid():  # Valida o formulário
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)  # Autentica o usuário

            if usuario is not None:  # Se o usuário for autenticado com sucesso
                auth.login(request, usuario)  # Realiza o login do usuário
                messages.success(request, f"{nome} Usuário Logado com sucesso")
                return redirect('index')  # Redireciona para a página inicial

            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')  # Se a autenticação falhar, redireciona de volta para a página de login

    return render(request, "usuarios/login.html", {"form": form})  # Renderiza o formulário de login


def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha_cadastro_1"].value() != form["senha_cadastro_2"].value():
                messages.error(request, "Senhas Não São Iguais")
                return redirect ('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email_cadastro'].value()
            senha=form['senha_cadastro_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existe")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})





def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    
    return redirect('login')