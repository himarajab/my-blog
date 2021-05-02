from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from .forms import PwdResetForm,pwdChangeForm


app_name = 'accounts'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profiles/',views.ProfileListView.as_view(),name='profile-list'),
    path('follow_unfollow/',views.follow_unfollow_profile,name='follow-unfollow'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate,name='activate'),
    # path('loin/',LoginView.as_view(),name='login'),
    path('my_login/',views.my_login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('detail/<pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('profile_update', views.profile_update, name='profile-update'),
    
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name= 'registration/password_change_form.html',form_class = pwdChangeForm),name='pwdforget'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name= 'registration/password_reset.html',form_class = PwdResetForm),name='pwdreset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name= 'registration/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name= 'registration/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name= 'registration/password_reset_done.html')
         ,name='password_reset_complete'),
    path('search/', views.PostSearchListView.as_view(), name='search-view'),
     
    ]