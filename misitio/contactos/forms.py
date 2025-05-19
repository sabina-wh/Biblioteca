from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    mensaje = forms.CharField(widget=forms.Textarea)

def clean_asunto(self):
    asunto = self.cleaned_data['asunto']
    if not asunto:
        raise forms.ValidationError('Ingresa el asunto de tu mensaje')
    return asunto

def clean_mensaje(self):
    mensaje=self.cleaned_data['mensaje']
    texto_mensaje = len(mensaje.split())
    if texto_mensaje < 5:
        raise forms.ValidationError('El mensaje debe contener minimo 5 palabras.')
    return mensaje