from django import forms #? Importando formulario por defecto de django para modificarlo
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User #? Importando el modelo de usuarios ya por defecto de django

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self, *args, **kwargs): #*Creando metodo para no duplicar email's
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists(): 
        #?Utilizando filter para comprobar si existe uno o mas emails con la misma direccion pero anidandolo con el exist solo comprobara si existe algun objeto con la misma direccion
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
            #? raise sirve para generar un error.
        return email