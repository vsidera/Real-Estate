from django.urls import path,include
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url
from django.urls import path,include,re_path

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('newlisting/', views.ListingView.as_view(), name="newlisting"),
    path('listing/', views.ListingView.as_view(), name="all-listings"),
    path('listing/<id>', views.ListingView.as_view(), name="listing"),
    path('viewbid/', views.BidView.as_view(), name="all-bids"),
    path('<id>/bid/', views.BidView.as_view(), name="bidlisting"),
    path('listing/<id>/newbid/', views.BidView.as_view(), name="newbid"),
    path('users/', views.UserView.as_view(), name="all-users"),
    path('api/tours/', views.ToursView.as_view()),    
    re_path(r'api/tours/tours-id/(?P<pk>[0-9]+)/$',views.ToursDetail.as_view()),
    # path('api/search/', views.UserListView.as_view()),
    path('api/enquiry/', views.EnquiryView.as_view()),
    path('api/enquiry/enquiry-id/int:<pk>/', views.EnquiryDetail.as_view()),
    url(r'api/tours/tours-id/(?P<pk>[0-9]+)/$',
        views.ToursDetail.as_view()),
    url(r'api/enquiry/enquiry-id/(?P<pk>[0-9]+)/$',
        views.EnquiryDetail.as_view()), 
]
