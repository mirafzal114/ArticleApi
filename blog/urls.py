from django.urls import path
from blog.views import (ArticleListCreate, ArticleRetrieveUpdateDestroy, TagListCreate,
                        CommentListCreate, CommentRetrieveUpdateDestroy, UserListCreate, UserRetrieveUpdateDestroy)


urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroy.as_view(), name='article-detail'),
    path('tags/', TagListCreate.as_view(), name='tag-list'),
    path('comments/', CommentListCreate.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view(), name='comment-detail'),
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]