from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    # path('',home,name='home'),
    path('search/',post_search,name='post-search'),
    path('post_follow_view/',posts_of_following_profiles,name='post-follow-view'),
    path('add_comment/',add_comment,name='add-comment'),

    path('liked/', like_unlike_post, name='like-post-view'),
    path('article/<int:id>',post_detail,name='article-details'),
    
    
    # path('like/<int:pk>',like_view,name='like-post'),

    # path('like/<int:id>',like_post,name='like_post'),
    
    # path('like/', like_post, name="like_post"),


    # path('dislike_detail/<int:id>',dislike_detail,name='dislike_detail'),

    path('fav<int:id>',favourite_add,name='favourite-add'),
    path('user/favourites',user_favourites,name='favourites'),
    
    path('add_post/',AddPostView.as_view(),name='add-post'),
    path('article/detail/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete-post'),
    # path('article/<int:pk>/delete',DeletePostView.as_view(),name='delete-post'),
    # name it what u want here and in the view
    path('<slug:post>/', post_single, name='post_single'),
    path('category/<category>/', CatListView.as_view(), name='category'),
]