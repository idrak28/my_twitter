
from django.contrib import admin
from django.urls import path
from django.conf import settings # static file
from django.conf.urls.static import static # static file


from . import views

urlpatterns = [
    #path("admin/", admin.site.urls),
  path('',views.index , name='index') ,
] 

