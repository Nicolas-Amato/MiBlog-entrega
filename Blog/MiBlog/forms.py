from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class autorForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    titulo = forms.CharField(max_length = 40)
    email = forms.EmailField(max_length=40)
    subtitulo = forms.CharField(max_length=100)
    post = forms.CharField(widget=forms.Textarea)



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}