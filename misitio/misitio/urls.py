"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from biblioteca import views
from biblioteca.views import (inicio, editores_list, editores_view, editores_modificar, editores_eliminar,
                              libros_list, libros_view, libros_modificar, libros_eliminar,
                              autores_list, autores_view, autores_modificar, autores_eliminar,
                              ListaEditores, CrearEditores, EditarEditores, BorrarEditores,
                              ListaAutores, CrearAutores, EditarAutores, BorrarAutores,
                              ListaLibros, CrearLibros, EditarLibros, BorrarLibros)
from misitio.views import hola, fecha_hoy, fechamx_hoy, horas_adelante, fecha_actual, fecha_actualizada, mipagina, fecha_futura
from contactos.views import contactanos, contactos, gracias
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Le decimos a Django que cualquier peticion a la url /hola/ sea manejada por la funcion de vista:/hola/ (no necesariamente tiene que llamarse igual)
    url (r'^hola/$',hola),
    url (r'^mipagina/$',mipagina),
    url (r'^fecha/$',fecha_hoy),
    url (r'^fechactual/$',fecha_actual),
    url (r'^fechactualizada/$',fecha_actualizada),
    url (r'^fechamx/$',fechamx_hoy),
    url(r'^fechafutura/(?P<horas>\d+)/$', fecha_futura),
    #Expresion regular (/d{1,2}) permitir numeros de 1 ó 2 digitos
    url (r'^fecha/mas/(\d{1,2})/$',horas_adelante),

    url(r'^formulario-buscar/$',views.formulario_buscar),
    url(r'^buscar/$',views.buscar),
    url(r'^contactanos/$',contactanos),
    url(r'^contactos/$',contactos, name='contactos'),
    url(r'^contactos/gracias/$',gracias),
    url(r'^inicio/$',inicio, name='inicio'),

#Basadas en clases (CBV)

    url(r'^editores/listar/$',ListaEditores.as_view(), name='editores_listar'),
    url(r'^editores/agregar/$',CrearEditores.as_view(), name='editores_agregar'),
    url(r'^editores/(?P<pk>[0-9]+)/editar/$',EditarEditores.as_view(), name='editores_editar'),
    url(r'^editores/(?P<pk>[0-9]+)/borrar/$',BorrarEditores.as_view(), name='editores_borrar'),

    url(r'^libros/listar/$', ListaLibros.as_view(), name='libros_listar'),
    url(r'^libros/agregar/$', CrearLibros.as_view(), name='libros_agregar'),
    url(r'^libros/(?P<pk>[0-9]+)/editar/$', EditarLibros.as_view(), name='libros_editar'),
    url(r'^libros/(?P<pk>[0-9]+)/borrar/$', BorrarLibros.as_view(), name='libros_borrar'),

    url(r'^autores/listar/$', ListaAutores.as_view(), name='autores_listar'),
    url(r'^autores/agregar/$', CrearAutores.as_view(), name='autores_agregar'),
    url(r'^autores/(?P<pk>[0-9]+)/editar/$', EditarAutores.as_view(), name='autores_editar'),
    url(r'^autores/(?P<pk>[0-9]+)/borrar/$', BorrarAutores.as_view(), name='autores_borrar'),
#Basadas en funciones
    url(r'^editores/mostrar/$', editores_list, name='editores_mostrar'),
    url(r'^editores/crear/$', editores_view, name='editores_crear'),
    url(r'^editores/modificar/(?P<id_editor>\d+)/$', editores_modificar, name='editores_modificar'),
    url(r'^editores/eliminar/(?P<id_editor>\d+)/$', editores_eliminar, name='editores_eliminar'),

    url(r'^libros/mostrar/$', libros_list, name='libros_mostrar'),
    url(r'^libros/crear/$', libros_view, name='libros_crear'),
    url(r'^libros/modificar/(?P<id_libro>\d+)/$', libros_modificar, name='libros_modificar'),
    url(r'^libros/eliminar/(?P<id_libro>\d+)/$', libros_eliminar, name='libros_eliminar'),

    url(r'^autores/mostrar/$', autores_list, name='autores_mostrar'),
    url(r'^autores/crear/$', autores_view, name='autores_crear'),
    url(r'^autores/modificar/(?P<id_autor>\d+)/$', autores_modificar, name='autores_modificar'),
    url(r'^autores/eliminar/(?P<id_autor>\d+)/$', autores_eliminar, name='autores_eliminar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Durante el modo desarrollo
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Se añade una nueva ruta a las URL del proyecto para poder acceder alos archivos del directorio media