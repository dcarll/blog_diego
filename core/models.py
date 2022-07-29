from django.db import models
from stdimage import StdImageField
import uuid
from usuarios.models import CustomUsuario
from django.contrib.auth import get_user_model

# Create your models here.
def get_file_path(_instance, filename):
	'''função para gerar um id unico, que será passado na hora de gerar no caminho e no da imagem'''
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'
	return filename

class Base(models.Model):
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Post(Base):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(get_user_model(), max_length=255, verbose_name='Autor', on_delete=models.CASCADE)
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {"width": 480, "height": 480, "crop": True}}, blank=True)

    def __str__(self):
        return self.titulo_post

    


class Sobre(Base):
    sobre = models.TextField()

    def __str__(self):
        return self.Sobre


