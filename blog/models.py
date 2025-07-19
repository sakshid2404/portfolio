from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    total_likes_count = models.IntegerField(default=0)

    

    # def total_likes(self):
    #     return self.likes.count()

   

    def __str__(self):
        return self.title
    

   

    
       