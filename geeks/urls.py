from django.urls import path
from .views import *
urlpatterns = [
    # path('setcookie/', setcookie,name='setcookie'),
    path('index/',Index.as_view(),name='index'),
]