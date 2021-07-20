from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from crum import get_current_user


class Page(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    #order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    pdf = models.FileField(upload_to='pages/pdfs/')
    cover = models.ImageField(upload_to='pages/covers/', null=True, blank=True)

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['updated']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        super(Page, self).save(*args, **kwargs)
    
    


#def