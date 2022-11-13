from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('register', views.UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    # path("get-details",views.UserDetailAPI.as_view()),
    # path("signin",views.LoginUserView.as_view()),
    # path('signup',views.RegisterUserAPIView.as_view()),
    path("customized/getuserdetails",views.UserDetailAPI.as_view()),
    path("customized/login",views.LoginUserView.as_view()),
    path('customized/createuser',views.RegisterUserAPIView.as_view()),
    path('', include('django_rest_allauth.api.urls')),

]
