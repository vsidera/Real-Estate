from django.shortcuts import render
from django.http  import HttpResponse
<<<<<<< HEAD
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer,EnquirySerializer
=======
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer, ToursSerializer
>>>>>>> a40918c037936f5fd679bf0718de251eb24c10da
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Profile, Listing, Tours
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
    permission_classes = (IsAuthenticated,IsCompanyAdmin) 
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class ToursView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
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
    permission_classes = (IsAuthenticated,IsCompanyAdmin) 
    def get_tour(self, pk):
        try:
            return Tours.objects.get(pk=pk)
        except Tours.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        tour = self.get_tour(pk)
        serializers = ToursSerializer(tour)
        return Response(serializers.data)     
 
    def put(self, request, pk, format=None):
        tour = self.get_tour(pk)
        serializers = ToursSerializer(tour, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tour = self.get_tour(pk)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



