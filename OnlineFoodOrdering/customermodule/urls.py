from django.contrib import admin
from django.urls import path,include
from . import views
from .views import viewfood
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewfood/',viewfood,name='viewfood'),
    path('viewfood1/',views.viewfood1,name='viewfood1'),
    path('southveg/',views.southveg,name='southveg'),
    path('deserts/',views.deserts,name='deserts'),
    path('review_list/',views.review_list,name='review_list'),
    path('add_review/',views.add_review,name='add_review'),
]