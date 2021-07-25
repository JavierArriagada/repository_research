from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    #list_display = ('updated')
    
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('articles/css/custom_ckeditor.css',)
        }
        
admin.site.register(Article, ArticleAdmin)