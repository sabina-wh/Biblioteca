from django import forms
from django.core.exceptions import ValidationError
from biblioteca.models import Editor, Libro, Autor
import datetime

class EditorForm(forms.ModelForm):
	class Meta:
		model = Editor
		fields = [
			'nombre',
			'domicilio',
			'ciudad',
			'estado',
			'pais',
			'website',
		]
		labels= {
    		'nombre': 'Nombre',
    		'domicilio': 'Domicilio',
    		'ciudad': 'Ciudad',
    		'estado': 'Estado',
    		'pais': 'Pais',
    		'website': 'SitioWeb',
    	}
		widgets = {
    		'nombre': forms.TextInput(attrs={'class':'form-control'}) ,
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
		}

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = [
			'titulo',
			'autores',
			'editor',
			'fecha_publicacion',
			'portada',
		]
		labels= {
			'titulo': 'Titulo',
			'autores': 'Autores',
			'editor': 'Editor',
			'fecha_publicacion': 'Fecha Publicacion',
			'portada': 'Portada',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control js-example-basic-multiple'}),
			'editor': forms.Select(attrs={'class': 'form-control form-select'}),
			'fecha_publicacion': forms.TextInput(attrs={'class':'form-control'}),
			'portada':forms.ClearableFileInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(LibroForm, self).__init__(*args, **kwargs)
		self.fields['editor'].choices = [("", "Selecciona un editor")] + [(editor.id, editor.nombre) for editor in Editor.objects.all()]
		self.fields['editor'].widget.attrs.update({'class': 'form-control'})

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		fields = [
			'nombre',
			'apellidos',
			'email',
		]
		labels= {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'email': 'Email',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}
