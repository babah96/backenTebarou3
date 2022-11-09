"""tebarrou3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_rest_allauth.api.urls')),
    path('', include('users.urls', namespace='users')),
]

# CORS_ALLOW_CREDENTIALS = True

# authenticatesocialuser [name='authenticatesocialuser']
# token/createuser [name='createuser']
# token/login [name='login']
    # he will return the ==> # Token token.......
    #  he will return a "message": "logged out successfully"
# token/getuser [name='getuser']
    # header => Token token.......
    #  he will return user information 
# token/edituser [name='edituser']
    # header => Token token.......
    # he will return user information with the possibility to change his information
# token/changepassword [name='changepassword']
    # header => Token token.......
    # {
    #     "old_password": "sidi1212",
    #     "new_password": "sidi1234"
    # }
    # he will return a "message": "password changed  successfully"
# token/resetpasswordcode [name='resetpasswordcode']
# token/resetpassword [name='resetpassword']
# token/logout [name='logout']
    # header => Token token.......
    # he will return a "message": "logged out successfully"
