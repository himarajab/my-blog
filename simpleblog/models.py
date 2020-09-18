from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255,default='uncategorized')

    def __str__(self):
        return self.name

    #     to ease redirection process after success submit (edit or post )

    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255,default='uncategorized')
    title_tag = models.CharField(max_length=255,default='home')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(default=timezone.now)
    post_update = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')


    class Meta:
        ordering = ['-id']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    #     to ease redirection process after success submit (edit or post )

    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    comment_date= models.DateTimeField(auto_now_add=True)
    # are the admin accept that comment or not
    active = models.BooleanField(default=False)
    # to connect the comment to the related post
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return '{} commented on {}'.format(self.name,self.post)

    class Meta:
        ordering = ['-comment_date']
