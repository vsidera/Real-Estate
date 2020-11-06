from django.urls import path,include,re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
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
    path('api/tours/tour-id/int:<pk>/', views.ToursDetail.as_view()),
]