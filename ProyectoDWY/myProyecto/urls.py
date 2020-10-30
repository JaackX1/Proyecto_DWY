from django.contrib import admin
from django.urls import path
from .views import index,galeria,formularios,insumos,mision,resenias,servicios,sucursales,usuario,login,cerrarSesion,lista_insumos,eliminar_insumo,buscar,modificar

urlpatterns = [
    path('',index,name='INDEX'),
    path('insumos/',insumos,name='INSUMOS'),
    path('insumos_admin/',lista_insumos,name='LISTAINSUMOS'),
    path('mision/',mision,name='MISION'),
    path('resenias/',resenias,name='RESENIAS'),
    path('servicios/',servicios,name='SERVICIOS'),
    path('sucursales/',sucursales,name='SUCURSALES'),
    path('usuario/',usuario,name='USUARIO'),
    path('galeria/',galeria,name='GALERIA'),
    path('formularios/',formularios,name='FORMULARIOS'),
    path('login/',login,name='LOGIN'),
    path('logout_sesion/',cerrarSesion,name='LOGOUT'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINARINSUMO'),
    path('buscar_in/<id>/',buscar,name='BUSCARINSUMO'),
    path('modificar/',modificar,name='MODIFICARINSUMO'),
    
]