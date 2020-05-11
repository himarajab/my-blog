from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/',views.register,name='register'),
    # path('loin/',LoginView.as_view(),name='login'),
    path('loin/',views.login_user,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

]