from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('listing', views.ListingViewSet)

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]