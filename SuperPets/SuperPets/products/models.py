from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class BrandModel(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = ("Marca")
        verbose_name_plural = ("Marcas")

    def __str__(self):
        return str(self.id) + '-' + self.name

    def get_absolute_url(self):
        return reverse("brandmodel_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    brand = models.ForeignKey("BrandModel", verbose_name=("Marca"), on_delete=models.CASCADE)
    description = RichTextField(verbose_name="Descripción del producto")
    image = models.ImageField('Imagen', upload_to="products", height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.SmallIntegerField(verbose_name="Cantidad almacen", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id', 'title']

    def __str__(self):
        return str(self.id) + '-' + self.title
