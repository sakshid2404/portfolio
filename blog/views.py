from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponseNotAllowed
from django.urls import reverse

from .models import Article 


class ArticleDetailView(DetailView):
    model = Article 
    template_name = 'blog/blog_detail.html' 
    context_object_name = 'article' 

   

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        
        context['total_likes'] = self.object.total_likes_count 
        return context


class ArticleLikeView(LoginRequiredMixin, View):
   

    def post(self, request, pk, *args, **kwargs):
       
        article = get_object_or_404(Article, pk=pk)

       
        article.total_likes_count += 1
        article.save()

        return redirect(reverse('blog_detail', args=[article.slug]))

    def get(self, request, pk, *args, **kwargs):
      
        return HttpResponseNotAllowed(['POST'])

   