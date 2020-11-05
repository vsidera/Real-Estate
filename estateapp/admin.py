from django.contrib import admin
from .models import User,Profile,Listing,Bid
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Listing)
admin.site.register(Bid)