from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer, UserSerializer,BidSerializer,BidListingSerializer,BidAdminSerializer, ToursSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .models import Profile, Listing, Bid, User, Tours
from .permissions import IsCompanyAdmin, IsNormalUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegisterView(APIView):
    def post(self, request, format=None):
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

class ListingView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = ListingSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    permission_classes = (IsAuthenticated,IsNormalUser)
    def get(request):
        try:
            listing_post = Listing.objects.all()
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ListingSerializer(listing_post, many=True)
            return Response(serializer.data)
    permission_classes = (IsAuthenticated,IsNormalUser)
    def get(request,id):
        try:
            listing_post = Listing.objects.get(id=id)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = ListingSerializer(listing_post)
            return Response(serializer.data)