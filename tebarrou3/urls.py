
from django.contrib import admin
from django.urls import path,include
# from django_rest_allauth.api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users', include('django_rest_allauth.api.urls')),
    # path('', include('users.urls', namespace='users')),
    path('urgence', include('urgence.urls', namespace='urgence')),
    path('user/', include('manageusers.urls')),
    path('', include('django_rest_allauth.api.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

# CORS_ALLOW_CREDENTIALS = True

# authenticatesocialuser [name='authenticatesocialuser']
# token/createuser [name='createuser']
# token/login [name='login']
    # he will return the ==> # Token token.......
    #  he will return a "message": "logged out successfully"
# token/getuser [name='getuser']
    # header => Token to`ken.......
    #  he will return user information 
# token/edituser [name='edituser']
    # header => Token token.......
    # he will return user information with the possibility to change his information
# token/changepassword [name='changepassword'] => POST
    # header => Token token.......
    # {
    #     "old_password": "sidi1212",
    #     "new_password": "sidi1234"
    # }
    # he will return a "message": "password changed  successfully"
# to reset password you shoud do 
    #1- token/resetpasswordcode [name='resetpasswordcode']
        # Post Email and reset code 
        # {
        #     "message": {
        #         "email": "mhdabdellahi2018@gmail.com",
        #         "resetcode": "11111"
        #     }
        # }
    #2- token/resetpassword [name='resetpassword']
        # Post your email and the resetcode reseted and your new password 
        # {
        #     "message": {
        #         "message": "password successfully set"
        #     }
        # } 
# token/logout [name='logout']
    # header => Token token.......
    # will be remove the token
    # he will return a "message": "logged out successfully"
