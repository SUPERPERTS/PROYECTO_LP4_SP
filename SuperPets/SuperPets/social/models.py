from django.db import models

# Create your models here.
class Link(models.Model):
    """Model definition for Link."""

    key = models.SlugField('Nombre clave', max_length=100, unique=True) # Nos obligrara a utulizar alfanumericos, guiones y barras y no usar espacios o especiales
    # Vamos a mapear estos enlaces dentro de la memoria de la pagina utilizando key, luego accederemos a ella como si fuera un diccionario
    name = models.CharField('Red social', max_length=200)
    url = models.URLField('Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField('Creado', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Actualizado', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Link."""

        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        """Unicode representation of Link."""
        return str(self.id) + '-' + self.name
