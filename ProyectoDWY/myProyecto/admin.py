from django.contrib import admin
from .models import SliderIndex,SliderGaleria,Insumos,MisionVision


# estilos admin

class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10

class SliderIndexAdmin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

class SliderGaleriaAdmin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

class MisionVisionAdmin(admin.ModelAdmin):
    list_display = ['ident','mision','vision']
    search_fields = ['ident']
    list_per_page = 10
    
# Register your models here.

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(SliderGaleria, SliderGaleriaAdmin)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(MisionVision, MisionVisionAdmin)

