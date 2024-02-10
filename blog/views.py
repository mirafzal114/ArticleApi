from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Article, Tag, Comment, Image
from .serializers import ArticleSerializer, TagSerializer, CommentSerializer, UserSerializer
# from paginations import StandardResultSetPagination
from rest_framework.exceptions import ValidationError

from rest_framework.pagination import PageNumberPagination

class StandardResultSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultSetPagination

class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()
        image_data = self.request.FILES.getlist('images')
        for image_data in image_data:
            Image.objects.create(article=instance, image=image_data)

    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user)
        except ValidationError as e:
            raise ValidationError({'detail': e.detail})

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
