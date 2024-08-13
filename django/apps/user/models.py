# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Custom User Manager
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Email is required')
#         if not username:
#             raise ValueError('Username is required')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, username, password=None, **extra_fields):
        
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             role = User.Role.ADMIN,
#             **extra_fields
#         )
#         user.save()
#         return user

# # Custom User Model
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(verbose_name='email', max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
    
#     # built in django fields
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         ordering = ['-last_login']