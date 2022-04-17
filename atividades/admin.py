from django.contrib import admin
from .models import blog
from .models import Cate_por_tipo

class Admblogecate(admin.ModelAdmin):
    list_display=("nome_do_autor")
    search_fields=['titulo']
    list_filter=("categoria")

admin.site.register([blog,Cate_por_tipo])
