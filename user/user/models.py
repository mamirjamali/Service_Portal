"""
Models related to user object.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserManager(BaseUserManager):
    """Defaine manager for base user model."""

    def create_user(self, email, username, password=None, **kwargs):
        """Create user method."""
        if not email:
            raise ValueError('User must have an email')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        """Create useruser method."""
        user = self.create_user(email, password, **kwargs)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Define base user model for system"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']
