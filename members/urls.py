from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('register/',views.register,name='register'),
    # path('loin/',LoginView.as_view(),name='login'),
    path('login/',views.login_user,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile-update'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name= 'accounts/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name= 'accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name= 'accounts/password_reset_done.html')
         ,name='password_reset_complete'),
    ]