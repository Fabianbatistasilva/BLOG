
from django.db import models
class Cate_por_tipo(models.Model):
    categoria=models.CharField(max_length=100,unique = True)
    def __str__(self) :
        return self.categoria
    class Meta:
        verbose_name_plural = 'Tipos'
class blog(models.Model):
    nome_do_autor=models.CharField(max_length=100)
    conteudo_blog=models.TextField(max_length=10000)
    titulo=models.CharField(max_length=100)
    imagem=models.ImageField(blank=True)
    publicado =models.DateTimeField(auto_now_add=True,blank=True)
    categoria=models.ForeignKey(Cate_por_tipo,on_delete=models.DO_NOTHING)
    def __str__(self) :
        return self.titulo
