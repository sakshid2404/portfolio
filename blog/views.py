from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse

def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article,
        'total_likes': article.total_likes_count,
       
    }
    return render(request, 'blog/blog_detail.html', context)



@login_required
def like_view(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)

        # Increment the count directly
        article.total_likes_count += 1
        article.save() # Save the changes to the database

        # Redirect back to the blog detail page using the article's slug
        return HttpResponseRedirect(reverse('blog_detail', args=[article.slug]))
    else:
        return HttpResponseNotAllowed(['POST'])