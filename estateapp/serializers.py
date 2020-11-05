from rest_framework import serializers
from .models import Profile, Listing, Enquiry
from django.contrib.auth import get_user_model
User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password','password2','role']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role = self.validated_data['role']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})

        user.set_password(password)
        user.save()

        return user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name', 'profile_picture', 'location']


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'Location', 'Price', 'Realtor', 'Image1', 'Image2', 'Image3', 'Image4','Bedrooms','Bathrooms']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        models = Enquiry
        fields = ['id','Message']