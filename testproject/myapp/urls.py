
from django.contrib import admin
from django.urls import path ,re_path
from . import views

urlpatterns = [
    # path('hello/<int:id>', views.hello ,name = 'hello'),
    path('hello/<int:id>', views.hello ,name = 'hello'),
    path('', views.index ,name = 'witaya'),
    re_path(r'article/(?P<year>[0-9]{4})$',views.article),
    re_path(r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$',views.article , name='article'),
]
