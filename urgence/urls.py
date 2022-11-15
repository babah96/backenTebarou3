from django.urls import path
from .import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('',views.UrgenceViewset,basename='urgence')
# urlpatterns=urlpatterns+router.urls
app_name='urgence'
urlpatterns=[
    # path('api_views',views.UrgenceList.as_view(), name="list")
    # path('api_views/', views.Medecinlist.as_view(), name='index'),
#     # path('medcinDtail/<int:id>/', views.MedcinDtail.as_view(), name='Emprunte'),
    
]
urlpatterns=urlpatterns+router.urls