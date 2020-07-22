from django.urls import path
from . import views

app_name = 'my_core'

urlpatterns = [
    path('', views.DataListView.as_view(), name='home'),
    path('add/', views.DataCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.DataUpdateView.as_view(), name='detail-data'),
    path('<int:pk>/delete/', views.DataDeleteView.as_view(), name='delete-data'),
    
    path('ar/', views.DataListView.as_view(), name='home_ar'),
    path('add_ar/', views.DataARCreateView.as_view(), name='add_ar'),
    path('<int:pk>/update_ar/', views.DataARUpdateView.as_view(), name='detail-data_ar'),
    path('<int:pk>/delete_ar/', views.DataARDeleteView.as_view(), name='delete-data_ar'),
    
]