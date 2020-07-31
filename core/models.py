from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

class Data(models.Model):
    title = models.CharField(max_length=255)
    # url = models.URLField( max_length=200)
    # i added to this field '' as default value and it worked fine   
    body = JSONField()    

    # By specifying self as the first parameter of the model.ForeignKey call, Django will set this up as a recursive relationship
    
    
    # parent = models.ForeignKey('self', 
    parent = models.ForeignKey('core.Data',
    null=True, on_delete=models.CASCADE)
    # body_json =JSONField(default = '')    
    Data_date = models.DateField(default=timezone.now)
    Data_update = models.DateField(auto_now=True)



    def __str__(self):
        return str(self.id)

    #     to ease redirection process after success submit (edit or Data )

    def get_absolute_url(self):
        return reverse('my_core:home')
        #  return reverse('my_core:data-detail', args=[self.id])



