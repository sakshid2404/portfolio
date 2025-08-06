from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView,CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Article 

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/create.html'
    fields = ['title', 'content', 'slug', 'image']
    success_url = reverse_lazy('index')


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


def get_queryset(self):
        return Article.objects.all().order_by('-created_at')
   