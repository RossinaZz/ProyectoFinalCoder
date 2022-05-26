from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from FinalGym.models import Avatar

class EntrenadorFormulario(forms.Form):
   
    nombre= forms.CharField()
    apellido=forms.CharField()
    matricula= forms.IntegerField()
    clase= forms.CharField()

class UsuarioFormulario(forms.Form):
    nombre=forms.CharField()
    numerocliente=forms.IntegerField()
    claseinscripta=forms.CharField()

class ClaseFormulario(forms.Form):
    nombre=forms.CharField()
    camada=forms.IntegerField()
    duracion=forms.IntegerField()

class RegistroFormulario(UserCreationForm):

    email= forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField()
    first_name= forms.CharField()

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name'] 
        help_texts = {k:"" for k in fields }

        
class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['user', 'imagen']
  