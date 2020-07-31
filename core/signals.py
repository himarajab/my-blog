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


# post_save.connect(customer_profile,sender= User)


def get_parent_object(child_title):
    
    result = None
    objects = Data.objects.filter(title=child_title).first()

    if objects.parent:
        result = objects.parent
    else:
        result = objects
    return result


@receiver(post_save,sender=Data)
def creat_profile(sender,instance,**kwargs):
    if kwargs['created']:
        # check the length of created objects to prevent max recuresion error
        # TODO: change the filtere attribute or add url 
        # to the title to prevent collisons and without minutes 
        # cause this way will lead to infinte instance creation
        # or make it unique
        objects = Data.objects.filter(title=instance.title)


        parent_object = get_parent_object(instance.title)
        
        

        # will add suportaded languages here to make objects equal to them
        # after detect post language i will create instances with suportaded language
        suporated_languages = 'ar','en','ru'

        if len(objects) < len(suporated_languages):
            Data.objects.create(
                parent = parent_object,
                title = instance.title,
                body = instance.body+'ar'
            )
        else:
            pass

# @receiver(post_save,sender=Data)
# def update_profile(sender,instance,created,**kwargs):
#     # if the object is updated 
#     if created == False:
#         # save the object to the db
#         instance.profile.save()
# post_save.connect(update_profile,sender=Data)