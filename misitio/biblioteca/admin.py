from django.contrib import admin
from biblioteca.models import Editor,Autor,Libro
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','email') #columnas que se mostraran al realizar cambios
    search_fields = ('nombre','apellidos')#Agregar barra de busqueda

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','editor','fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    #fields = ('titulo','autores','editor','portada')
    #filter_horizontal = ('autores',)
    filter_vertical = ('autores',)#utilizar solamente con campos ManyToManyField
    raw_id_fields = ('editor',)#opcion para campos ForeingKey

admin.site.register(Editor)
admin.site.register(Autor,AutorAdmin)#Registar el modelo Autor con opciones de Autoradmin
admin.site.register(Libro,LibroAdmin)