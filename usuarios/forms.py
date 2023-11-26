from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                "placeholder": "Ex: João Silva",}
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite Sua Senha",}
        )
    )
    
    
class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome Completo",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                "placeholder": "Ex: João Silva Pereira",}
        )
    )
    
    email_cadastro = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                "placeholder": "Ex: joaosilva@xpto.com",}
        )
    )
    senha_cadastro_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite Sua Senha",}
        )
    ) 
    senha_cadastro_2 = forms.CharField(
        label="Confirme Sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite Sua Senha Novamente",}
        )
    )
