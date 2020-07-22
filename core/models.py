from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save


class Data(models.Model):
    title = models.CharField(max_length=255)
    # url = models.URLField( max_length=200)    
    body = models.TextField(null=True,blank=True)

    # body_json =JSONField(default = '')
    # body_json =JSONField(blank=True, null=True,default=dict)
    
    Data_date = models.DateField(default=timezone.now)
    Data_update = models.DateField(auto_now=True)



    def __str__(self):
        return self.title 

    #     to ease redirection process after success submit (edit or Data )

    def get_absolute_url(self):
        return reverse('my_core:home')
        #  return reverse('my_core:data-detail', args=[self.id])



class Data_ar(models.Model):
    title = models.CharField(max_length=255)
    # url = models.URLField( max_length=200)    
    body = models.TextField(null=True,blank=True)
    Data_date = models.DateField(default=timezone.now)
    Data_update = models.DateField(auto_now=True)



    def __str__(self):
        # {self.title} posted
        return self.body  

    #     to ease redirection process after success submit (edit or Data )

    def get_absolute_url(self):
        return reverse('my_core:home')








