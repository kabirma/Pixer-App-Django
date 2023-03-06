from django.urls import path, include
from .views import *
urlpatterns = [
    path('blog/categories/<str:search>',blogCategories),
    path('blogs/',blogs)
]
