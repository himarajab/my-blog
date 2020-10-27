from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    # path('',home,name='home'),
    path('like/<int:id>/',PostLikeToggle.as_view(),name='like-toggle'),
    path('article/<int:id>',post_detail,name='article-details'),
    path('api/<int:id>',PostLikeAPIToggle.as_view(),name='like-api-toggle'),
    
    # path('like/<int:pk>',like_view,name='like-post'),

    # path('like/<int:id>',like_post,name='like_post'),
    
    # path('like/', like_post, name="like_post"),


    # path('dislike_detail/<int:id>',dislike_detail,name='dislike_detail'),

    path('user/favourites',user_favourites,name='favourites'),
    
    path('add_post/',AddPostView.as_view(),name='add-post'),
    path('article/detail/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete-post'),
    # path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete-post'),
    # name it what u want here and in the view
    path('category/<str:cats>',category_view,name='category'),
    path('category_list',category_list_view,name='category-list'),
]