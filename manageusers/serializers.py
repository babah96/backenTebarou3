from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django_rest_allauth.api.serializers import UserLoginSerializer

class LoginSerializer(UserLoginSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    def validate(self, data):
        # email = data['email']
        if not 'email' in data and not 'username' in data :
            raise serializers.ValidationError('Enter Username Or Email')        
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', "username","password", "email", "first_name", "last_name","is_admin","is_simpleUser","phone","blood_type","weight","height","birth","gender")
        # fields = '__all__'

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name',"is_admin","is_simpleUser","phone","blood_type","weight","height","birth","gender")
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      is_admin= validated_data['is_admin'],
      is_simpleUser = validated_data['is_simpleUser'],
      phone= validated_data['phone'],
      blood_type = validated_data['blood_type'],
      weight= validated_data['weight'],
      height = validated_data['height'],
      birth= validated_data['birth'],
      gender = validated_data['gender']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user