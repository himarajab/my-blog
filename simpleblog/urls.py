from django.urls import path
# from .views import HomeView,ArticleDetailView
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    path('add_post/',AddPostView.as_view(),name='add-post'),
]