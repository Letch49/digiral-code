from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_teacher, **extra_fields):
        print(extra_fields)
        email = self.normalize_email(email)
        user = self.model(email=email, is_teacher=is_teacher, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, is_teacher, **extra_fields) -> 'User':
        return self._create_user(email=email, password=password, is_teacher=is_teacher, **extra_fields)

    def create_superuser(self, email, password, **extra_fields) -> 'User':
        return self._create_user(email=email, password=password, is_superuser=True, is_teacher=True, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField('superuser', default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def get_token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def str(self) -> str:
        return self.email
