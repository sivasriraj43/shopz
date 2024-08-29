from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    USER_TYPE={
        ("Seller","Seller"),
        ("Buyer","Buyer"),
        ("Deeler","Deeler"),
    }
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    user_type=models.CharField(max_length=20,choices=USER_TYPE, default='Buyer',verbose_name='User Type')
    img=models.FileField(upload_to='image-path',null=True,blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

@receiver(post_save,sender=User)
def profile_create(sender,created,instance,**kwargs):
    if created:
        profile=Profile.objects.create(user=instance)
        profile.save()
   

 