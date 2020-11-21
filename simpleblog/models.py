from mptt.models import MPTTModel,TreeForeignKey
from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'posts/%Y/%m/%d/'.format(instance.id, filename)



class Category(models.Model):
    name = models.CharField(max_length=255,default='uncategorized')

    def __str__(self):
        return self.name

    #     to ease redirection process after success submit (edit or post )

    def get_absolute_url(self):
        return reverse("article-details", kwargs={"id": self.id})


class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    excerpt = models.TextField(null=True)

    title = models.CharField(max_length=255)
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    category = models.CharField(max_length=255,default='uncategorized')
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/default.jpg')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager



    class Meta:
        ordering = ['-id']

    def total_likes(self):
        return self.liked.all()

    def __str__(self):
        return self.title + '|' + str(self.author)

    #     to ease redirection process after success submit (edit or post )

    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse("article-details", kwargs={"id": self.id})

    def num_likes(self):
        return self.liked.all().count()



class Comment(MPTTModel):
  
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    # to access the subcomments on comment
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True ,related_name='children')
    # excerpt = models.TextField(null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_inseration_by = ['publish']

    def __str__(self):
        return f'Comment by {self.name}'


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"