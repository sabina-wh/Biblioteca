from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from biblioteca.models import Autor,Libro, Editor
from biblioteca.forms import EditorForm, LibroForm, AutorForm
# Create your views here.

def inicio(request):
    return render(request,'biblioteca/index.html')

def formulario_buscar(request):
    return render(request,'formulario_buscar.html')

#def buscar(request):
#    if 'q' in request.GET and request.GET['q']:#Verificar que el valor de q exista y que no sea una cadena vacia
#        q = request.GET['q']#Almacena el valor q
#        #Buscar en la BD todos los objetos Libro donde campo titulo contenga el valor de q
#        libros =Libro.objects.filter(titulo__icontains=q)#consulta a la tabla libros icontains es una busqueda (case-insensitive)
#        # REnderiza la plantilla y envia como contexto los resultados Libros y el termino de busqueda q
#        return render(request,'resultados.html',{'libros':libros,'query':q})
#    else:
#        #return HttpResponse('Por favor introduce un termino de búsqueda.')
#        return render (request,'formulario_buscar.html',{'error':True})
#def buscar(request):
#    error=False
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if not q:
#            error=True
#        else:
#            libros = Libro.objects.filter(titulo__icontains=q)
#            return render(request, 'resultados.html', {'libros': libros, 'query': q})
#    return render(request,'formulario_buscar.html', {'error':error})

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de búsqueda')
        elif len(q) > 20:
            errors.append('El termino de busqueda debe ser menor a 20 caracteres')
        else:
            libros=Libro.objects.filter(titulo__icontains=q)
            return render(request, 'resultados.html', {'libros': libros, 'query': q})
    return render(request, 'formulario_buscar.html', {'errors': errors})

class ListaEditores(ListView):
    model = Editor
    template_name = 'biblioteca/editor_listar.html'
    ordering = ['id']
#Django usa el form_valid() de SuccessMessageMixin primero, lo cual añade el mensaje de éxito,
# y luego llama al metodo padre (createView).
class CrearEditores(SuccessMessageMixin,CreateView):
    model = Editor
    form_class = EditorForm
    #fields = ['nombre', 'domicilio', 'ciudad', 'estado', 'pais', 'website']
    template_name = 'biblioteca/editor_agregar.html'
    success_url = reverse_lazy('editores_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Editor fue agregado exitosamente')
        return super().form_valid(form)

class EditarEditores(SuccessMessageMixin,UpdateView):
    model = Editor
    form_class = EditorForm
    #fields = ['nombre', 'domicilio', 'ciudad', 'estado', 'pais', 'website']
    template_name = 'biblioteca/editor_agregar.html'
    success_url = reverse_lazy('editores_listar')
    #success_message = "Editor actualizado exitosamente."
#definir el metodo de validacion del formulario para mostrar un mensaje de exito confiable
    def form_valid(self, form):
        messages.success(self.request, 'Editor ha sido actualizado exitosamente')
        return super().form_valid(form)

class BorrarEditores(DeleteView):
     model = Editor
     template_name = 'biblioteca/editor_borrar.html'
     success_url = reverse_lazy('editores_listar')

     def delete(self, request, *args, **kwargs):
         messages.error(self.request, 'El Editor fue eliminado exitosamente')
         return super().delete(request, *args, **kwargs)

class ListaLibros(ListView):
    model = Libro
    template_name = 'biblioteca/libro_listar.html'
    ordering = ['titulo']

class CrearLibros(SuccessMessageMixin,CreateView):
    model = Libro
    form_class = LibroForm
    #fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada']
    template_name = 'biblioteca/libro_agregar.html'
    success_url = reverse_lazy('libros_listar')

    def form_valid(self, form):
        messages.success(self.request, 'El Libro fue agregado exitosamente')
        return super().form_valid(form)

class EditarLibros(SuccessMessageMixin,UpdateView):
    model = Libro
    form_class = LibroForm
    #fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada']
    template_name = 'biblioteca/libro_agregar.html'
    success_url = reverse_lazy('libros_listar')
    def form_valid(self, form):
        messages.success(self.request, 'El libro ha sido actualizado exitosamente')
        return super().form_valid(form)

class BorrarLibros(DeleteView):
     model = Libro
     template_name = 'biblioteca/libro_borrar.html'
     success_url = reverse_lazy('libros_listar')
     def delete(self, request, *args, **kwargs):
         messages.error(self.request, 'El Libro fue eliminado exitosamente')
         return super().delete(request, *args, **kwargs)

class ListaAutores(ListView):
    model = Autor
    template_name = 'biblioteca/autor_listar.html'
    ordering = ['apellidos']

class CrearAutores(SuccessMessageMixin,CreateView):
    model = Autor
    form_class = AutorForm
    #fields = ['nombre', 'apellidos', 'email']
    template_name = 'biblioteca/autor_agregar.html'
    success_url = reverse_lazy('autores_listar')

    def form_valid(self, form):
        messages.success(self.request, 'El Autor fue agregado exitosamente')
        return super().form_valid(form)

class EditarAutores(SuccessMessageMixin,UpdateView):
    model = Autor
    form_class = AutorForm
    #fields = ['nombre', 'apellidos', 'email']
    template_name = 'biblioteca/autor_agregar.html'
    success_url = reverse_lazy('autores_listar')
    def form_valid(self, form):
        messages.success(self.request, 'El Autor ha sido actualizado exitosamente')
        return super().form_valid(form)

class BorrarAutores(DeleteView):
     model = Autor
     template_name = 'biblioteca/autor_borrar.html'
     success_url = reverse_lazy('autores_listar')

     def delete(self, request, *args, **kwargs):
         messages.error(self.request, 'El Autor fue eliminado exitosamente')
         return super().delete(request, *args, **kwargs)

#Vistas Basadas en Funciones
def editores_list(request):
    editores = Editor.objects.all().order_by('id')
    return render(request, 'biblioteca/editor_mostrar.html', {'editores': editores})

def editores_view(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='El Editor ha sido agregado.')
            return redirect('editores_mostrar')
    else:
        form = EditorForm()
    return render(request, 'biblioteca/editor_form.html', {'form': form})

def editores_modificar(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        form = EditorForm(request.POST,instance=editor)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS,message='Tus modificacciones han sido actualizadas')
            return redirect('editores_mostrar')
    else:
        form = EditorForm(instance=editor)
    return render(request, 'biblioteca/editor_form.html', {'form': form})

def editores_eliminar(request,id_editor):
    editores=Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        editores.delete()
        messages.add_message(request=request, level=messages.ERROR, message='El Editor ha sido eliminado')
        return redirect('editores_mostrar')
    return render(request, 'biblioteca/editor_eliminar.html', {'editores': editores})

def libros_list(request):
    libros = Libro.objects.all().order_by('titulo')
    return render(request, 'biblioteca/libro_mostrar.html', {'libros': libros})

def libros_view(request):
    if request.method == 'POST':
        form = LibroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='El libro ha sido agregado.')
            return redirect('libros_mostrar')
    else:
        form = LibroForm(initial={'editor': ''})
    return render(request, 'biblioteca/libro_form.html', {'form': form})

def libros_modificar(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        form = LibroForm(request.POST,instance=libro)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS,message='Tus modificacciones han sido actualizadas')
            return redirect('libros_mostrar')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/libro_form.html', {'form': form})

def libros_eliminar(request,id_libro):
    libros=Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        libros.delete()
        messages.add_message(request=request, level=messages.ERROR, message='El Libro ha sido eliminado')
        return redirect('libros_mostrar')
    return render(request, 'biblioteca/libros_eliminar.html', {'libros': libros})

def autores_list(request):
    autores = Autor.objects.all().order_by('apellidos')
    return render(request, 'biblioteca/autor_mostrar.html', {'autores': autores})

def autores_view(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message='El Autor ha sido agregado.')
            return redirect('autores_mostrar')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/autor_form.html', {'form': form})

def autores_modificar(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST,instance=autor)
        if form.is_valid():
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS,message='Los datos del Autor han sido modificados.')
            return redirect('autores_mostrar')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/autor_form.html', {'form': form})

def autores_eliminar(request,id_autor):
    autores=Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        autores.delete()
        messages.add_message(request=request, level=messages.ERROR, message='El Autor ha sido eliminado')
        return redirect('autores_mostrar')
    return render(request, 'biblioteca/autor_eliminar.html', {'autores': autores})