from django.contrib import admin
from .models import User,Profile,Listing,Bid,Tours,Enquiry
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Tours)
admin.site.register(Enquiry)
