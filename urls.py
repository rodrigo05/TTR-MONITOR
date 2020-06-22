from django.contrib import admin
from django.urls import include, path

from . import views

#
from django.conf import settings
from django.conf.urls.static import static
#
urlpatterns = [
     path('', views.index, name='index'),
     #path('upload_doc', views.upload_doc, name='upload_doc'),
     #path('post/new', views.post_new, name='post_new'),
     path('demo/', views.demo, name='demo'),
     path('dealer/', views.dealer, name='dealer'),
     path('cliente/', views.cliente, name='cliente'),

     path('calendar/', views.calendar, name='calendar'),
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
