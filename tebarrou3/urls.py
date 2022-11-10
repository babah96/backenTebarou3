
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
