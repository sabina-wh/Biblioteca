import datetime #modulo de python que proporciona clases para manipular fechas y horas.
import locale # modulo de python para trabajar con configurtaciones regionales del S.O
from django.template.loader import get_template
#from django.template import Template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
# utilizar """...""" permite escribir texto que ocupe varias líneas sin necesidad de usar \n para saltos de línea.
#Cadena de texto multilinea
#HTML = """
#<!DOCTYPE html>
#<html lang="es">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Hola mundo</title>
#   <style type="text/css">
#    html * {padding:0;margin:0;}
#    body * {padding:10px 20px;}
#    body ** {padding:0;}
#    body {font:small sans-serif;}
#    body>div {border-bottom:1px solid #ddd;}
#    h1 {font-weight:normal;}
#    #summary {background:#e0ebff;}
#    </style>
#</head>
#<body>
#    <div id="summary">
#    <h1>Hola mundo</h1>
#    <p>Bienvenido:Este es el contenido de la página.</p>
#   </div>
#</body>
#</html>
#"""

def hola(request):
    return HttpResponse(HTML)

"""
cada funcion de vista o vista , toma la menos un parametro llamado por convencion request.

El cual es un objeto que contiene informacion sobre la la vista que llama a la pagina acual , la cual es una instancia de la clase django.http.HttpRequest.
"""

def fecha_hoy(request):
    ahora = datetime.datetime.now()
    fecha = "<html><body><h1>Fecha:</h1><h3>%s</h3></body></html>"%ahora
    return HttpResponse(fecha)

def fechamx_hoy(request):
    #Cambiar o consultar la configuracion regional(locale)
    locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')#Utilizar la configuracion regional español mexico para fecha y hora
    fecha_hoy = datetime.datetime.now() # Funcion que se utiliza para obtener la fecha y hora actual del sistema
    fecha_mx = fecha_hoy.strftime("%d de %B de %Y")
    #metodo strftime para formatear objetos de fecha en cadenas legibles.
    hora_mx = fecha_hoy.strftime("%H:%M")
    #String format (f-string)
    #fechamx = f"""
    #    <html>
    #    <body>
    #        <h1>Fecha:</h1>
    #        <h3>{fecha_mx}</h3>
    #        <h1>Hora:</h1>
    #        <h3>{hora_mx}</h3>
    #    </body>
    #    </html>
    #    """
    # Usar .format() en lugar de f-string
    fechamx = """
            <html>
            <body>
                <h1>Fecha:</h1>
                <h3>{}</h3>
                <h1>Hora:</h1>
                <h3>{}</h3>
            </body>
            </html>
            """.format(fecha_mx, hora_mx)
    return HttpResponse(fechamx)

def horas_adelante(request, offset):#offset es el parametro (numero entero) que representa la cantidad de horas a sumar a la hora actual
    try:
        offset = int(offset)#conversion cadena de caracteres a entero
    except ValueError: # Si el valor no es tipo entero
        raise Http404()# Se produce un error
    #datetime.timedelta representa una duracion o diferencia de tiempo
    #horanext = fecha y hora actual + la suma del numero de horas correspondiente
    horanext = datetime.datetime.now()+datetime.timedelta(hours=offset)# parametro horas debe ser tipo entero
    hora_next = "<html><body><h1>En %s hora(s), seran:</h1><h3>%s</h3></body></html>"%(offset,horanext)
    return HttpResponse(hora_next)
"""
def fecha_actual(request):
    actual = datetime.datetime.now()
    t = Template("<html><body>Hoy es {{fecha_actual}}</body></html>")
    html=t.render(Context({'fecha_actual':actual}))
    return HttpResponse(html)
    
def fecha_actual(request):
    actual = datetime.datetime.now()
    # forma simple de usar platillas del sistema de archivos
    # Pero es malo, porque no tama en cuenta los archivos no encontrados
    fp = open ('/home/sabina-cano/Documentos/ambientes/misitio/misitio/templates/miplantilla.html')
    t = Template(fp.read())
    fp.close()
    html=t.render(Context({'fecha_actual':actual}))
    return HttpResponse(html)   
    
"""
def fecha_actual(request):
    actual = datetime.datetime.now()
    t = get_template('miplantilla.html')
    html = t.render(Context({'fecha_actual':actual}))
    return HttpResponse(html)

def fecha_actualizada(request):
    actualizada = datetime.datetime.now()
    return render(request,'fecha_actual.html',{'fecha_actualizada':actualizada})

def mipagina(request):
    contexto = {
        'titulo': 'Bienvenido a mi sitio',
        'seccion_actual': 'inicio',
    }
    return render(request,'mipagina.html',contexto)

def fecha_futura(request,horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    datime=datetime.datetime.now()+datetime.timedelta(hours=horas)
    return render(request,'fecha_adelante.html',{'hora_siguiente':datime,'horas':horas})
