import django.http
from django.core.mail import send_mail #permite el envio email
from django.http import HttpResponseRedirect
from django.shortcuts import render

from contactos.forms import FormularioContactos


def contactanos(request):
    errors = [] #Almacenar los errores
    if request.method == "POST": #Verificar la solicitus es un envio de formulario
        if not request.POST.get('asunto'):
            errors.append('Por favor, introduce el asunto')
        if not request.POST.get('mensaje'):
            errors.append('Por favor, introduce el mensaje')
        if request.POST.get('email') and '@' not in request.POST.get('email'):#email deben contener @ para ser valido
            errors.append('Por favor, introduce una direccion email valida')
        if not errors:#Si no se encontarron errores
            send_mail(request.POST['asunto'],request.POST['mensaje'],#se envia email con los datos
             request.POST.get('email','noreply@example.com'),#email del usuario
             ['siteowner@example.com'],)#destinatario del formulario
            return HttpResponseRedirect('/contactos/gracias')#si envio es exitoso redirige a pagina de agradecimiento
    return render(request, 'form-contact.html', {'errors': errors})# si la solicitud no es POST o hay errores se muestra nuevamente el formulario

def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)#Crea una instancia del formulario usando datos que envio usuario
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com']
            )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={'mensaje':'¡Dejanos tus comentarios!'})
    return render(request, 'formulario-contactos.html', {'form': form})


#def contactos(request):
#    errors = []
#    if request.method == "POST":
#        if not request.POST.get('asunto'):
#            errors.append('Por favor, introduce el asunto')
#        if not request.POST.get('mensaje'):
#            errors.append('Por favor, introduce el mensaje')
#        if request.POST.get('email') and '@' not in request.POST.get('email'):
#            errors.append('Por favor, introduce una direccion email valida')
#       if not errors:
#           send_mail(request.POST['asunto'],request.POST['mensaje'],
#             request.POST.get('email','noreply@example.com'),
#             ['siteowner@example.com'],)
#            return HttpResponseRedirect('/contactos/gracias')
#    return render(request, 'formulario-contactos.html', {'errors': errors,
#                                                         'asunto': request.POST.get('asunto',""),
#                                                        'mensaje': request.POST.get('mensaje',""),
#                                                         'email': request.POST.get('email',""),
#                                                        })

def gracias(request):
    return render(request, 'contactos-gracias.html')