from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={'id': 'usern', 'name':'username', 'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'pwd', 'name':'password', 'class':'form-control'})
    )