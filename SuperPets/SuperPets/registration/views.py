from django.shortcuts import render
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationFormWithEmail

    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        #*Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contrasenia'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contrasenia'})
        return form 