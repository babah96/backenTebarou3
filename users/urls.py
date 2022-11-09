from django.urls import path
from .views import UserRecordView, UserViewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user',UserViewset,basename='users')

app_name = 'users'
urlpatterns = [
    
    path('', UserRecordView.as_view(), name='users'),
]
urlpatterns=urlpatterns+router.urls