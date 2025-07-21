from django.shortcuts import render
from blog.models import Article

def index(request):
    Articles = Article.objects.all()
    return render(request, 'website/index.html',{'articles': Articles})

def resume_view(request):
    return render(request, 'website/resume.html')