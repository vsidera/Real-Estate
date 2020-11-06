from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
class User(AbstractUser):
    USER_ROLES = (
        ('CA', 'COMPANY ADMIN'),
        ('NU', 'NORMAL USER')
    )
    role = models.CharField(
        verbose_name='user role', max_length=2, choices=USER_ROLES,default='NU'
    )

    