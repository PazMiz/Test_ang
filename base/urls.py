from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import register
from .views import public_view
from .views import admin_only_view


urlpatterns = [
   
   path('',  views.index),
   path('about',  views.about),
   path('products',views.products_view.as_view()),
   path('products/<pk>',views.products_view.as_view()),
   path('login/', TokenObtainPairView.as_view()),
    path('register/', register, name='register'),
    path('public/', public_view, name='public-view'),
    path('admin-only/', admin_only_view, name='admin-only-view'),
    

    

]
