from django.contrib import admin
from registration.models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user', 'link')
    
    # Inyectamos nuestro fichero css
    class Media:
        css = {
        'all': ('profiles/css/custom_ckeditor.css',)
        }
        
admin.site.register(Profile, ProfileAdmin)