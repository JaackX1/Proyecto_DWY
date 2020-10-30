from django.shortcuts import render
from .models import SliderGaleria,SliderIndex,Insumos,MisionVision

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
def index(request):
    sliders = SliderIndex.objects.all()
    return render(request,'web/index.html',{'imagenes':sliders})

# =============================
def galeria(request):
    sliders = SliderGaleria.objects.all()
    return render(request,'web/galeria.html',{'imagenes':sliders})

# =============================
def mision(request):
    lista = MisionVision.objects.all()
    return render(request,'web/mision.html',{'lista':lista})

# =============================
def resenias(request):
    return render(request,'web/resenias.html')


# =============================
def servicios(request):
    return render(request,'web/servicios.html')


# =============================
def sucursales(request):
    return render(request,'web/sucursales.html')

# =============================
def formularios(request):
    return render(request,'web/formularios.html')


# |=============================|
# | INSUMOS     |    INSUMOS    |
# |=============================|
@login_required(login_url='/login/')
@permission_required('myProyecto.view_insumos',login_url='/login/')
def lista_insumos(request):
    lista = Insumos.objects.all()
    return render(request,'web/insumos_admin.html',{'lista_insumos':lista})

# =============================

@login_required(login_url='/login/')
@permission_required('myProyecto.view_insumos',login_url='/login/')
@permission_required('myProyecto.delete_insumos',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='ELIMINO INSUMO'
    except:
        msg= 'NO ELIMINO'

    lista = Insumos.objects.all()
    return render(request,'web/insumos_admin.html',{'lista_insumos':lista,'msg':msg})

# =============================

@login_required(login_url='/login/')
def buscar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/insumos_mod.html',{'insumo':insumo})

    except:
        msg = 'NO EXISTE INSUMO'
        
    lista = Insumos.objects.all()
    return render(request,'web/insumos_admin.html',{'lista_insumos':lista,'msg':msg})

# =============================

@login_required(login_url='/login/')
@permission_required('myProyecto.view_insumos',login_url='/login/')
@permission_required('myProyecto.change_insumos',login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtInsumo")
        stock = request.POST.get("txtStock")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg = 'MODIFICADO'
        
        except:
            msg = 'NO MODIFICADO'

        lista = Insumos.objects.all()
        return render(request,'web/insumos_admin.html',{'lista_insumos':lista,'msg':msg})

# =============================
@login_required(login_url='/login/')
@permission_required('myProyecto.add_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("txtInsumo")
        stock = request.POST.get("txtStock")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
            
        )

        insumo.save()
        return render(request,'web/insumos.html',{'msg':'INSUMO GRABADO'})

    return render(request,'web/insumos.html')


# |=============================|
# | USUARIO     |    USUARIO    |
# |=============================|
def usuario(request):
    if request.POST:
        nombre = request.POST.get("txtNombreRegistro")
        apellido = request.POST.get("txtApellidoRegistro")
        email = request.POST.get("txtCorreoRegistro")
        usuario = request.POST.get("txtUsuarioRegistro")
        pass1 = request.POST.get("txtPass1Registro")
        pass2 = request.POST.get("txtPass2Registro")

        if pass1!=pass2:
            return render(request,'web/usuario.html',{'msg':'CLAVES INCORRECTAS'})

        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/usuario.html',{'msg':'USUARIO YA EXISTE'})

        except:
            try:
                usu = User.objects.get(email=email)
                return render(request,'web/usuario.html',{'msg':'EMAIL YA EXISTE'})
            except:
                usu = User()

                usu.first_name = nombre
                usu.last_name = apellido
                usu.email = email
                usu.username = usuario
                usu.set_password(pass1)
                usu.save()

                usu = authenticate(request,username=usuario, password=pass1)
                login_autent(request,usu)
                sliders = SliderIndex.objects.all()
                return render(request,'web/index.html',{'imagenes':sliders})

    return render(request,'web/usuario.html')


# =============================
def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuarioLogin")
        password1 = request.POST.get("txtPassLogin")

        usu = authenticate(request,username=usuario, password=password1)

        if usu is not None and usu.is_active:
            login_autent(request,usu)
            sliders = SliderIndex.objects.all()
            return render(request,'web/index.html',{'imagenes':sliders})
        else:
            return render(request,'web/login.html',{'msg':'no existe usuario'})
    return render(request,'web/login.html')


# =============================
def cerrarSesion(request):
    logout(request)
    sliders = SliderIndex.objects.all()
    return render(request,'web/index.html',{'imagenes':sliders})