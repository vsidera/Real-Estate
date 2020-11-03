from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = CloudinaryField('image')
    
    def __str__(self):
            return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)    

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()        

class Listing(models.Model):
    ''' a model for Listing '''

    Location = models.CharField(max_length=150)
    Price = models.IntegerField()
    Realtor = models.CharField(max_length=150)
    Image1 = CloudinaryField('image')
    Image2 = CloudinaryField('image')
    Image3 = CloudinaryField('image')
    Image4 = CloudinaryField('image')
    Bedrooms = models.IntegerField()
    Bathrooms = models.IntegerField()

class Bid(models.Model):
    ''' a model for Listing '''

    Bidamount = models.IntegerField()
    User = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='bidder')
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing')


class Enquiry(models.Model):
    ''' a model for Listing '''

    Message = models.IntegerField()
    User = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='enquirer')
   

        
   


