from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Data(models.Model):
    title = models.CharField(max_length=255)
    # url = models.URLField( max_length=200)    
    body = models.TextField(null=True,blank=True)
    Data_date = models.DateField(default=timezone.now)
    Data_update = models.DateField(auto_now=True)



    def __str__(self):
        return self.title 

    #     to ease redirection process after success submit (edit or Data )

    def get_absolute_url(self):
        return reverse('my_core:home')
        #  return reverse('my_core:data-detail', args=[self.id])



    # def delete(self, *args, **kwargs):
    #     # delete the file saved in the db to override 
    #     self.pdf.delete()
    #     self.cover.delete()
    #     super().delete(*args, **kwargs)
