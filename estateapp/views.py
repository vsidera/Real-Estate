from django.shortcuts import render
from django.http  import HttpResponse
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer, ToursSerializer,EnquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Profile, Listing, Tours, User, Enquiry
from .permissions import IsCompanyAdmin, IsNormalUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics

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
    permission_classes = (IsAuthenticated,IsCompanyAdmin) 
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class ToursView(APIView):
    
    def get(self, request, format=None):
        all_tours = Tours.objects.all()
        serializers = ToursSerializer(all_tours, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ToursSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

class ToursDetail(APIView):
    
    def get_tours(self, pk):
        try:
            return Tours.objects.get(pk=pk)
        except Tours.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        tours = self.get_tours(pk)
        serializers = ToursSerializer(tours)
        return Response(serializers.data)     
 
    def put(self, request, pk, format=None):
        tours = self.get_tours(pk)
        serializers = ToursSerializer(tours, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tours = self.get_tours(pk)
        tours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EnquiryView(APIView):
    # permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def get(self, request, format=None):
        all_enquiries = Enquiry.objects.all()
        serializers = EnquirySerializer(all_enquiries, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = EnquirySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

class EnquiryDetail(APIView):
    # permission_classes = (IsAuthenticated,IsCompanyAdmin) 
    def get_enquiry(self, pk):
        try:
            return Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        enquiry = self.get_enquiry(pk)
        serializers = EnquirySerializer(enquiry)
        return Response(serializers.data)     
 
    def put(self, request, pk, format=None):
        enquiry = self.get_enquiry(pk)
        serializers = EnquirySerializer(enquiry, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        enquiry = self.get_enquiry(pk)
        enquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



