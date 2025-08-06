from django.urls import path
from .views import ArticleDetailView, ArticleLikeView , ArticleCreateView

urlpatterns = [
 
    path('slug:<slug:slug>/', ArticleDetailView.as_view(), name='blog_detail'),
    path('like/<int:pk>/', ArticleLikeView.as_view(), name='like_post'),
    path('create/', ArticleCreateView.as_view(), name='create_blog'),
]