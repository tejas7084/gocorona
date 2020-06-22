from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='home'),
    path('globe/',views.globe,name='globe'),
    path('about_us/',views.about_us,name='about_us'),
    path('facts_page/',views.facts_page, name='facts-page')
]
