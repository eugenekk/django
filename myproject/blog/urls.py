from django.urls import path, include, register_converter
from . import views
from .converters import CodeConverter

register_converter(CodeConverter, 'dddd')

urlpatterns = [
    path('test/', views.index),
    path('test2/<dddd:id>', views.test2), # id라는 인자를 받아서 씀
]
