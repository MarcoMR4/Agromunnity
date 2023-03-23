from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms

from .models import user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={'id': 'username', 'name':'username', 'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password', 'name':'password', 'class':'form-control'})
    )

class AddEmplooye(forms.Form):

    Nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6 ', 'style': 'font-size: 12px;','required':'true'}
        )
    )
    AP = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    AM = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )
    Correo = forms.CharField(
        widget=forms.TextInput(
            attrs={'name':'correo', 'class': 'form-control col-sm-6', 'style': 'font-size: 12px;', 'placeholder':'Debe contener dominio @morelia.tecnm.mx'}
        )
    )
    users = user.TIPOUSER
    tU = list(users)
    tU.pop(0)
    Tipo = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        ),
        choices=tU
    )
    Telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-sm-6', 'style': 'font-size: 12px;'}
        )
    )