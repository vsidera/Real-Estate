from rest_framework import serializers
from .models import Profile, Listing, Tours, Enquiry
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
