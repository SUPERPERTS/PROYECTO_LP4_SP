""" PROCESADOR DE CONTEXTO practicamente lo utilizamos para agregar variables globales a los templates """
from .models import Link

def ctx_dict(request):
    """Esta funcion obtiene los links de redes sociales y poder visualizarlos en todos los templates

    Args:
        request (string): Peticion

    Returns:
        obj: Objeto con todos los links que hay en la db
    """

    ctx = {}
    links = Link.objects.all() #? Creando objeto de Link
    for link in links:
        ctx[link.key] = link.url #?Creando un diccionario con las claves y valores que hay registrados en la tabla Link

    return ctx