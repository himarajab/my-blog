from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    image = models.ImageField(default='default.png',upload_to='profile_pic/')
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile'.format(self.user.username)

    # to decrease image size
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            outputsize = 300,300
            img.thumbnail(outputsize)
            img.save(self.image.path)


# to create profile once the user created
def creat_profile(sender,**kwargs):
    if kwargs['created']:
         Profile.objects.create(
            user = kwargs['instance']
        )

post_save.connect(creat_profile,sender=User)
