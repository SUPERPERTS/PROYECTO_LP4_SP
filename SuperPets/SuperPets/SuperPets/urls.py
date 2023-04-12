"""SuperPets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from products.urls import products_patterns

urlpatterns = [
    #* PATH de la App Core 
    path('', include('core.urls')),
    #* PATH de la App Products
    path('products/', include( products_patterns )), #*Cambio el formato de las urls y ahora se agregara dos puntos despues de pages para las urles de pages
    #* PATH del Admin
    path('admin/', admin.site.urls),
    #* Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

]

# Setencia para importar y que pueda servir archivos estaticos
if settings.DEBUG: # If DEBUG is True so do this...
    from django.conf.urls.static import static # importando static de las urls
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # static(URL, ROOT)
    # Le cedimos a la url que si alguine intenta acceder a la direccion de algun fichero, se lo sirva
