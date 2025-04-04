from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(label="Usuário", required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))

    password = forms.CharField(label="Senha", required=True, max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))