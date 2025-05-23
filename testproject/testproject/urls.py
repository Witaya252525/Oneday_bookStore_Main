"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path ,re_path ,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('myapp.urls','myapp'),namespace ='myapp')),
    path('book/', include(('book.urls','book'),namespace ='book')),
#     re_path(r'article/(?P<year>[0-9]{4})$',views.article),
#     re_path(r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$',views.article , name='article'),
    
]
# +static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

if settings.DEBUG :
    #static/media
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
