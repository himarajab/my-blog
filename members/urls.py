from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),

]