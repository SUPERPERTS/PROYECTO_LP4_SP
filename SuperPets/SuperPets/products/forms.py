from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("title", "description", "price", "id")
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese un título...'}), 
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'id': forms.NumberInput(attrs={'class':'form-control'})
        }
        #? Labels nos sirve para esconder el nombre de los campos y sustituirlos por el que queramos
        labels = {
            'title':'Titulo',
            'price':'Precio',
            'content':'Contenido de la pagina',
            'id':'Orden',
        }