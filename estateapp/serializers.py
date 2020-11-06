from rest_framework import serializers
from .models import Profile, Listing
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name', 'profile_picture', 'location']


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'Location', 'Price', 'Realtor', 'Image1', 'Image2', 'Image3', 'Image4','Bedrooms','Bathrooms']

