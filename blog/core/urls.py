from tkinter.font import names

from django.contrib import admin

from django.urls import path

from .views import *

urlpatterns = [

    path('', main, name='main'),

    path('more/<int:post_id>/', more, name="more")


]