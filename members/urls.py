from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('register/',views.register,name='register'),
    # path('loin/',LoginView.as_view(),name='login'),
    path('login/',views.login_user,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile-update'),
]