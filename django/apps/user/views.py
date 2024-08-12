from distutils.log import Log
import stat
from rest_framework.response import Response
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserCreateSerializer, UserRetrieveSerializer
from dj_rest_auth.views import UserDetailsView as BaseUserDetailsView
from django.contrib.auth import get_user_model

from Strapseeker_Backend.permissions import IsAdminUser, IsStaffUser
from Strapseeker_Backend.mixins import PaginationMixin


User = get_user_model()

class CustomRegisterView(RegisterView):
    # Anyone can register
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # Call the parent post method to perform registration
        response = super().post(request, *args, **kwargs)
        # Customize the response
        if response.status_code == status.HTTP_204_NO_CONTENT:
            # Modify response status code to 201 (Created)
            response.status_code = status.HTTP_201_CREATED
            
            # Fetch user data manually
            # You might need to adjust this based on your User model and serializer
            username = request.data.get('username')
            email = request.data.get('email')
            user = User.objects.get(username=username, email=email)

            # Successful registration
            data = {
                'success': True,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                'message': 'Registration successful'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            # Failed registration
            data = {
                'success': False,
                'message': 'Registration failed'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class CustomLogoutView(LogoutView):
    # Anyone can logout
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # Call the parent post method to perform logout
        authenticated = request.user.is_authenticated
        response = super().post(request, *args, **kwargs)
        # Customize the response

        # Check if the user is already logged out by verifying if the session is still active
        if response.status_code == status.HTTP_200_OK:
            print(authenticated)
            if not authenticated:
                data = {
                    'success': True,
                    'message': 'You are already logged out'
                }
                return Response(data)
            else:
                data = {
                    'success': True,
                    'message': 'Successfully logged out'
                }
                return Response(data)
        else:
            data = {
                'success': False,
                'message': 'Logout failed'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(LoginView):
    # Anyone can login
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # Call the parent post method to perform login
        response = super().post(request, *args, **kwargs)
        # Customize the response
        if response.status_code == 200 and 'key' in response.data:
            # Successful login
            user = self.request.user
            data = {
                'success': True,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                'token': response.data['key'],
                'message': 'Login successful'
            }
            return Response(data)
        else:
            # Failed login
            data = {
                'success': False,
                'message': 'Invalid email or password'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)