from django.shortcuts import render
# importar las tablas para trabajar en la VIEWS
from .models import TipoMascota, Mascota, galeria

# para trabajar con la tabla de usuarios importaremos User
from django.contrib.auth.models import User

# importar la libreria de autentificacion
from django.contrib.auth import authenticate,logout,login as login_autent
# importar la libreria de decoradores para la autentificacion
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
def crear_usuario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        nom_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")

        if pass1!=pass2:
            contexto = {"mensaje":"password no son iguales"}
            return render(request,"crear_usuario.html",contexto)

        usu = User()
        usu.first_name = nombre
        usu.last_name = apellido
        usu.email= email
        usu.username = nom_usuario
        usu.set_password(pass1)
        usu.save()

        contexto = {"mensaje":"grabo usuario"}
        return render(request,"crear_usuario.html",contexto)

    return render(request,"crear_usuario.html")

def index(request):
    mascotas = Mascota.objects.filter(publicar=True).order_by('-nombre')[:3]
    contexto = {"mascotas":mascotas}
    return render(request, "index.html",contexto)

def cerrar_sesion(request):
    logout(request)
    mascotas = Mascota.objects.filter(publicar=True).order_by('-nombre')[:3]
    contexto = {"mascotas":mascotas}
    return render(request,"index.html",contexto)

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombre")
        password = request.POST.get("txtPass")
        us = authenticate(request,username=usuario, password=password)
        if us is not None and us.is_active:
            login_autent(request,us) # almacenar usuario en el request
            return render(request,"index.html")
        else:
            contexto = {"mensaje":"usuario o contraseña incorrecta"}
            return render(request,"login.html",contexto)
    return render(request,"login.html")

def filtro_tipo_boton(request, id):
    tipos = TipoMascota.objects.all()   
    tip = request.POST.get("cboTipo")
    obj_tipo = TipoMascota.objects.get(nombre=id)
    mascotas = Mascota.objects.filter(tipo=obj_tipo).filter(publicar=True)
    cant = Mascota.objects.filter(tipo=obj_tipo).filter(publicar=True).count()
    contexto = {"mascotas":mascotas,"tipos":tipos,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def filtro_tipo(request):
    mascotas = Mascota.objects.filter(publicar=True) 
    cant = Mascota.objects.filter(publicar=True).count()
    tipos = TipoMascota.objects.all()
    if request.POST:
        tip = request.POST.get("cboTipo")
        obj_tipo = TipoMascota.objects.get(nombre=tip)
        mascotas = Mascota.objects.filter(tipo=obj_tipo).filter(publicar=True)
        cant = Mascota.objects.filter(tipo=obj_tipo).filter(publicar=True).count()
    contexto = {"mascotas":mascotas,"tipos":tipos,"cantidad":cant}
    return render(request, "galeria.html",contexto)

def filtro_descripcion(request):
    mascotas = Mascota.objects.all() # select * from Mascota
    tipos = TipoMascota.objects.all()
    if request.POST:
        texto = request.POST.get("txtTexto")
        mascotas = Mascota.objects.filter(descripcion__contains=texto).filter(publicar=True)
    contexto = {"mascotas":mascotas,"tipos":tipos}
    return render(request, "galeria.html",contexto)

def galerias(request):
    mascotas = Mascota.objects.filter(publicar=True)
    tipos = TipoMascota.objects.all()
    contexto = {"mascotas":mascotas,"tipos":tipos}
    return render(request, "galeria.html",contexto)

def detalle_mascota(request, id):
    mas = Mascota.objects.get(nombre=id)
    contexto = {"mascota":mas}
    galerias = galeria.objects.filter(mascota=mas)
    contexto["galerias"]=galerias
    cant = galeria.objects.filter(mascota=mas).count()
    contexto["cant"]= cant
    return render(request,"ficha.html", contexto)

@login_required(login_url='/login/')
@permission_required('misPerris.delete_mascota',login_url='/login/')
def eliminar_mascota(request,id):
    nom_user = request.user.username
    try:
        mas = Mascota.objects.get(nombre=id)
        mas.delete()
        mensaje = "Elimino Mascota"
    except:
        mensaje = "No encontro mascota"
    tipos = TipoMascota.objects.all()
    mascotas = Mascota.objects.filter(usuario=nom_user)
    contexto = {"mensaje":mensaje,"tipos":tipos,"mascotas":mascotas}
    return render(request, "formulario.html",contexto)

@login_required(login_url='/login/')
@permission_required('misPerris.view_mascota',login_url='/login/')
def buscar(request, id):
    try:
        mas = Mascota.objects.get(nombre=id)
        tipos = TipoMascota.objects.all()
        contexto = {"mascota":mas,"tipos":tipos}
        return render(request,"modificar.html",contexto)
    except:
        mensaje = "No encontro mascota"
    tipos = TipoMascota.objects.all()
    mascotas = Mascota.objects.all()
    contexto = {"mensaje":mensaje,"tipos":tipos,"mascotas":mascotas}
    return render(request, "formulario.html",contexto)

@login_required(login_url='/login/')
@permission_required('misPerris.add_mascota',login_url='/login/')
def formulario(request):
    nom_user = request.user.username # recupero nombre del usuario
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre").lower()
        try:
            m = Mascota.objects.get(nombre=nombre)
            mensaje ="Existe Perro"
        except:
            edad = request.POST.get("txtEdad")
            desc = request.POST.get("txtDesc")
            imagen = request.FILES.get("txtImg")
            tipo = request.POST.get("cboTipo") # Perro, Gatos , Pajaros
            # buscamos el registro asociado a el nombre de tipo mascota
            obj_tipoMascota = TipoMascota.objects.get(nombre=tipo) 
            mas = Mascota()
            mas.nombre=nombre
            mas.edad=edad
            mas.descripcion=desc
            if imagen is not None:
                mas.imagen=imagen

            mas.tipo=obj_tipoMascota
            mas.usuario= nom_user
            
            mas.save()
            mensaje="grabo"


    tipos = TipoMascota.objects.all() # select * from TipoMascota
    mascotas = Mascota.objects.filter(usuario=nom_user)   
    contexto={"tipos":tipos,"mascotas":mascotas,"mensaje":mensaje}
    return render(request, "formulario.html",contexto)

def insertar_imagen(request):
    mensaje=''
    x = 0
    if request.POST:
        m = request.POST.get("txtMascota")
        im = request.FILES.get("txtIma")
        mas = Mascota.objects.get(nombre=m)
        gale = galeria()
        gale.imagen = im
        gale.mascota = mas
        gale.save()
        mensaje='Grabado'
        x = 1
    
    nom_user = request.user.username # recupero nombre del usuario
    tipos = TipoMascota.objects.all() # select * from TipoMascota
    mascotas = Mascota.objects.filter(usuario=nom_user)   
    contexto={"tipos":tipos,"mascotas":mascotas,"mensaje":mensaje}
    return render(request, "formulario.html",contexto)



@login_required(login_url='/login/')
@permission_required('misPerris.change_mascota',login_url='/login/')
def formulario_modificar(request):
    nom_user = request.user.username
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        edad = request.POST.get("txtEdad")
        desc = request.POST.get("txtDesc")
        tipo = request.POST.get("cboTipo") # Perro, Gatos , Pajaros
        obj_tipoMascota = TipoMascota.objects.get(nombre=tipo)
        try:
            m = Mascota.objects.get(nombre=nombre)

            imagen = request.FILES.get("txtImg")
            
            if imagen is None:                 
                m.edad=edad
                m.descripcion=desc
                m.tipo=obj_tipoMascota
                m.comentario='--'
                m.save()
                mensaje="modifico"
            else: 
                m.edad=edad
                m.descripcion=desc
                m.tipo=obj_tipoMascota
                m.imagen= imagen
                m.comentario='--'
                m.save()
                mensaje="modifico"
        except:
            mensaje ="No se puede modificar"

    tipos = TipoMascota.objects.all() # select * from TipoMascota
    mascotas = Mascota.objects.filter(usuario=nom_user)

    contexto={"tipos":tipos,"mascotas":mascotas,"mensaje":mensaje}
    return render(request, "formulario.html",contexto)

@login_required(login_url='/login/')
def adoptar(request,id):
    try:
        mas = Mascota.objects.filter(publicar=True).get(nombre=id)
        mas.publicar = False
        mas.dueno = request.user.username
        mas.comentario = "Adoptada"
        mas.save()
        mensaje = "Adoptada"
        contexto = {"mensaje":mensaje,"mascota":mas}
        return render(request,"ficha.html",contexto)
    except:
        mensaje = "No Encontro Mascota"
        contexto = {"mensaje":mensaje}
        mascotas = Mascota.objects.filter(publicar=True).order_by('-nombre')[:3]
        contexto["mascotas"]=mascotas
        return render(request,"index.html",contexto)
    
@login_required(login_url='/login/')
def adm_usuario(request):
    nom_user = request.user.username
    mascotas = Mascota.objects.filter(dueno=nom_user)
    contexto = {"mascotas":mascotas}
    return render(request,"adm_usuario.html",contexto)

@login_required(login_url='/login/')
def devolver(request, id):
    mensaje=""
    try:
        mas = Mascota.objects.filter(publicar=False).get(nombre=id)
        mas.comentario='--'
        mas.dueno=''
        mas.save()
        mensaje="mascota devuelta"
    except:
        mensaje="error al devolver"
    nom_user = request.user.username
    mascotas = Mascota.objects.filter(dueno=nom_user)
    contexto = {"mascotas":mascotas,"mensaje":mensaje}
    return render(request,"adm_usuario.html",contexto)