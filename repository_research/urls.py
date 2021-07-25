"""repository_research URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles.urls import articles_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from django.conf import settings

urlpatterns = [
    #Path core
    path('', include('core.urls')),
    #Path Articles
    path('articles/', include(articles_patterns)),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    
    path('admin/', admin.site.urls),

    #Path de Auth
    path('accounts/', include('django.contrib.auth.urls')), #django nos proveera de diferentes urls para hacer la autentificacion
    path('accounts/', include('registration.urls')),

    #Paths de Messenger
    path('messenger/', include(messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)