from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('like/<int:pk>',views.like_view, name='like_post'),
]

