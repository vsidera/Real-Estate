from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import ProfileSerializer, ListingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Listing
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):

        content = {'message': 'Hello, World!'}
        return Response(content)