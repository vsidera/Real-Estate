from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import ProfileSerializer, ListingSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .models import Profile, Listing
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to Real Estate')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer