from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponse
from FinalGym.forms import AvatarFormulario, ClaseFormulario, EntrenadorFormulario, RegistroFormulario
from FinalGym.forms import UsuarioFormulario
from FinalGym.models import Entrenador
from FinalGym.models import Clase
from FinalGym.models import Usuario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from FinalGym.models import Avatar



#Registro

def register(request):

    if request.method == 'POST':

        form = RegistroFormulario(request.POST)

        if form.is_valid():

            user = form.cleaned_data['username']
            form.save()

            return render (request, "FinalGym/inicio.html", {'mensaje':"Usuario Creado"})

    else:

        form = RegistroFormulario()

    return render(request, "FinalGym/registro.html", {'form':form})

  #Inicio de sesion

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario= form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user:

                login(request, user)

                return render(request, 'FinalGym/inicio.html', {'mensaje': f"Bienvenido {user}"})

        else:

            return render(request,'FinalGym/inicio.html', {'mensaje:'"Error. Datos Incorrectos"})

    else :

        form = AuthenticationForm()

    return render(request, "FinalGym/login.html", {'form': form})

#Pagina de Inicio

def inicio(request):

    return render(request, "FinalGym/inicio.html")

#Vista para subir Avatares

def agregarImagen(request):

    if request.method == 'POST': 

        miFormulario = AvatarFormulario(request.POST, request.FILES) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = Avatar(user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, "FinalGym/inicio.html")

    else:

        miFormulario = AvatarFormulario()
    
    return render(request, "FinalGym/agregarImg.html", {'form':miFormulario})

#Vista para agregar Clases

def agregarClase(request):

    
    if request.method == 'POST':    

        miFormulario = ClaseFormulario(request.POST)    

        

        if miFormulario.is_valid():     

            informacion = miFormulario.cleaned_data

            clase = Clase(nombre=informacion['nombre'], camada=informacion['camada'], duracion=informacion['duracion'])  

            clase.save()

            return render(request, "FinalGym/inicio.html")  

    else:

        miFormulario = ClaseFormulario() 

    dict1={"miFormulario":miFormulario}

    return render(request, "FinalGym/clase.html", dict1)

#Vista para agregar Usuarios

@login_required
def agregarUsuario(request):

    return render(request, "FinalGym/usuario.html")

#Vista para agregar entrenadores


def agregarEntrenador(request):


    if request.method == 'POST':    #al hacer click en enviar

        miFormulario = EntrenadorFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data    #almacenos la informacion del formulario como diccionario

            trainer = Entrenador(nombre=info['nombre'], apellido=info['apellido'],
            matricula=info['matricula'],clase=info['clase'])

            trainer.save()

            return render(request, "FinalGym/inicio.html")

    else:

        miFormulario = EntrenadorFormulario()

    dict1={'myForm':miFormulario}

    return render(request,"FinalGym/entrenador.html", dict1)

#Vista para buscar Camadas

@login_required
def busquedaCamada(request):

    return render(request, "FinalGym/busquedaCamada.html")

@login_required
def buscar(request):

    #respuesta=f"Estoy buscando la camada {request.GET['camada']}"

    if request.GET['camada']:

        camada = request.GET['camada']      
        clases = Clase.objects.filter(camada__iexact=camada)

        return render(request, "FinalGym/resultadosBusqueda.html", {"clases":clases, "camada":camada})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)

#Vista para borrar entrenadores

@login_required
def borrarEntrenadores(request, entrenador_nombre):

    entrenador = Entrenador.objects.get(nombre=entrenador_nombre)
    
    entrenador.delete()
    
    entrenadores = Entrenador.objects.all()

    contexto={"entrenadores":entrenadores}

    return render(request, "FinalGym/leerEntrenadores.html",contexto)

#Vista para editar Entrenadores

@login_required
def editarEntrenadores(request, entrenador_nombre):

    entrenador= Entrenador.objects.get(nombre=entrenador_nombre)

    if request.method == "POST":

        miFormulario= EntrenadorFormulario(request.POST)

        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            entrenador.nombre = informacion['nombre']
            entrenador.apellido = informacion['apellido']
            entrenador.matricula = informacion['matricula']
            entrenador.clase = informacion['clase']

            entrenador.save()

            return render(request, "FinalGym/inicio.html")
    
    else: 
        
        miFormulario = EntrenadorFormulario(initial={'nombre':entrenador.nombre, 'apellido':entrenador.apellido, 'matricula':entrenador.matricula, 'clase':entrenador.clase})

    return render(request, "FinalGym/editarEntrenador.html", {'miFormulario':miFormulario, 'entrenador_nombre':entrenador_nombre})

#Vista para Editar Usuarios 

@login_required
def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST": 

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data  

          
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "FinalGym/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "FinalGym/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})



#Vista para mostrar a los Entrenadores

@login_required
def listaEntrenadores(request):

    entrenadores = Entrenador.objects.all() 

    contexto = {"entrenadores":entrenadores}
    return render(request, "FinalGym/leerEntrenadores.html",contexto)

#Vista para mostrar About

def Aboutus(request):
    return render(request, "FinalGym/about-us.html")

#Vista para mostrar a las clases/Clases

class ClaseList(LoginRequiredMixin, ListView):

    model = Clase
    template_name = "FinalGym/listaClases.html"

#Vista para mostrar detalle de las clases/Clase 

class ClaseDetalle(DetailView):

    model = Clase
    template_name = "FinalGym/claseDetalle.html"

#Vista para crear clases/Clase

class ClaseCreacion(CreateView):

    model = Clase
    success_url = "/FinalGym/clase/lista"
    fields = ['nombre', 'camada', 'duracion']

#Vista para mostrar actualizacion de las clases/Clase

class ClaseUpdate(UpdateView):

    model = Clase
    success_url = "/FinalGym/clase/lista"
    fields = ['nombre', 'camada', 'duracion']

#Vista para borrar clases/Clase

class ClaseDelete(DeleteView):

    model = Clase
    success_url = "/FinalGym/clase/lista"

#Vista para mostrar las clases/Clase

class UsuarioList(LoginRequiredMixin, ListView):

    model = Usuario
    template_name = "FinalGym/listaUsuario.html"




