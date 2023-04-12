from django.shortcuts import render
from django.views.generic.base import TemplateView

#* Usando las CBV Vistas Basadas en Clases

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs): #?Como buena practica a la hora de sobreescribir metodos, siempre debemos pasarle los argumentos *args y argumentos clave-valor **kwargs
        return render(request, self.template_name, {'title':'SuperPets'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"