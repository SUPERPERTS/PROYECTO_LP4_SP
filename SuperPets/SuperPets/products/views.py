from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required #? Decorador
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm

""" class StaffRequiredMixin(object):
    # TODO Mixin 
    # Es una implementacion de una o varias funcionalidades para una clase, podemos crearla una vez y heredar su comportamiento 
    # donde queramos y darle prioridad a su implementacion antes que a la otra clase.

    @method_decorator(staff_member_required) # Utilizando el decorador de identificacion
    def dispatch(self, request, *args, **kwargs): # Dispatch nos sirve para controlar la propia peticion
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) # En caso que SI este identificado redirecciona donde debe ser

    class Meta:
        abstract = True """


class ProductListView(ListView):
    model = Product

class ProductView(TemplateView):
    template_name = "products/products.html"

class ProductDetailView(DetailView):
    model = Product

@method_decorator(staff_member_required, name='dispatch') #? Para decorar el metodo Dispatch
class ProductCreateView(CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products')
    
@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('products:update', args=[self.object.id]) + '?ok' #? El '?ok' es un truco para indicar que todo ha ido bien 
        #? Este relajo es para obtener el id y de esta manera una vez actualizado los datos regresar a la pagina de update

@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products')
    
