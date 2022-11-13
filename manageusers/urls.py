from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('register', views.UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path("get-details",views.UserDetailAPI.as_view()),
    path("signin",views.LoginUserView.as_view()),
    path('signup',views.RegisterUserAPIView.as_view()),

]
