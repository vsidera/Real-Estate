from django.contrib import admin
from .models import User,Profile,Listing,Bid, Enquiry,Tours
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Enquiry)
admin.site.register(Tours)