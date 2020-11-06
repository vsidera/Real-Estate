from django.http  import HttpResponse
from .serializers import RegistrationSerializer, ProfileSerializer, ListingSerializer, UserSerializer,BidSerializer,BidListingSerializer,BidAdminSerializer, ToursSerializer,EnquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .models import Profile, Listing, Bid, User, Tours,Enquiry
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

class UserView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def get(request):
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
class BidView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def post(request,id):
        try:
            listing_post = Listing.objects.get(id=id)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            serializer = BidAdminSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticated,IsNormalUser)
    def put(request, id):
        try:
            bid_post = Bid.objects.get(id=id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = BidListingSerializer(bid_post,data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.erroBidListingSerializerrs,status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAuthenticated,IsNormalUser)
    def get(request):
        try:
            bid_post = Bid.objects.all()
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = BidSerializer(bid_post,many=True)
            return Response(serializer.data)
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
class EnquiryView(APIView):
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
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
    permission_classes = (IsAuthenticated,IsCompanyAdmin)
    def get_enquiry(self, pk):
        try:
            return Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        tour = self.get_tour(pk)
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