from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    #list_display = ('updated')
    
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }
        
admin.site.register(Page, PageAdmin)