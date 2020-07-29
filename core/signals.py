from django.db.models.signals import post_save
from .models import Data
from django.dispatch import receiver

# def customer_profile(sender, instance , created , **kwargs):
#     if created:
#         group = Group.objects.get(name='customer')
#         instance.groups.add(group)
#         Customer.objects.create(
#             user=instance,
#             name=instance.username,
#         )
#         print('profile created')


# post_save.connect(customer_profile,sender= User)


@receiver(post_save,sender=Data)
def creat_profile(sender,**kwargs):
    if kwargs['created']:
        print(f'\n{kwargs}signals\n')
        
        #  Data_ar.objects.create(
        #     user = kwargs['instance']
        # )


# @receiver(post_save,sender=Data)
# def update_profile(sender,instance,created,**kwargs):
#     # if the object is updated 
#     if created == False:
#         # save the object to the db
#         instance.profile.save()
# post_save.connect(update_profile,sender=Data)