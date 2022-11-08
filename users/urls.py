from django.urls import path
from .views import UserRecordView

app_name = 'users'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
]