from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Profile, Listing
from .permissions import IsCompanyAdmin, IsNormalUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST',])
def registration_view(request):

    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "success registration"
        data['email'] = user.email
        data['username'] = user.username
        data['role'] = user.role
    else:
        data = serializer.errors
    
    return Response(data)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,IsNormalUser) 
    def get(self, request):
        
        content = {'message': 'Hello, World!'}
        return Response(content)

