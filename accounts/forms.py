from django import forms

class LoginForms(forms.Form):
    
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuário',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha',
                'class': 'form-control'
            }
        )
    )


class SignupForms(forms.Form):
    
    username = forms.CharField(
        label="Usuário",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuário',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha',
                'class': 'form-control'
            }
        )
    )

    confirm_password = forms.CharField(
        label="Confirmar Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar Senha',
                'class': 'form-control'
            }
        )
    )