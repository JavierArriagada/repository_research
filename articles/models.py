from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from crum import get_current_user


class Article(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    pdf = models.FileField(upload_to='articles/pdfs/', max_length=200)
    #cover = models.ImageField(upload_to='articles/covers/', null=True, blank=True)

    class Meta:
        verbose_name = "artículo"
        verbose_name_plural = "artículos"
        ordering = ['updated']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        super(Article, self).save(*args, **kwargs)