from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.conf import settings
from .models import User

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

# for customizing dj-rest-auth registration fields
class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(required=True, choices=User.Role.choices)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['role'] = self.validated_data.get('role', '')
        return data_dict
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value
    

class CustomLoginSerializer(LoginSerializer):
    username = None
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        error_messages={
            'required': 'Please enter your password',
            'blank': 'Please enter your password',
        }
    )

    def validate(self, attrs):
        # Check if the user is already logged in
        if self.context['request'].user.is_authenticated:
            raise serializers.ValidationError("You are already logged in.")
        
        # Call the parent class' validate method
        return super().validate(attrs)