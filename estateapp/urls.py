from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url
from django.urls import path,include,re_path

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registration_view, name="register"),
    path('api/tours/', views.ToursView.as_view()),
    path('api/enquiry/', views.EnquiryView.as_view()),
    
    url(r'api/tours/tours-id/(?P<pk>[0-9]+)/$',
        views.ToursDetail.as_view()),
    url(r'api/enquiry/enquiry-id/(?P<pk>[0-9]+)/$',
        views.EnquiryDetail.as_view()),    
]

