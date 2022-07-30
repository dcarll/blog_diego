from django.contrib import admin
from .models import Sobre, Post

# Register your models here.

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
	list_display = ()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo_post', 'autor_post', 'conteudo_post', 'slug', 'imagem', )
