from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

def custom_upload_to(instance, filename):
    old_instance = Article.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'articles/' + filename

class Article(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    resume = RichTextField(verbose_name="Resumen")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    cover = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    
    class Meta:
        verbose_name = "articulo"
        verbose_name_plural = "articulos"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
