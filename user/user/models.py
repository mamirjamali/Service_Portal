"""
Models related to user object
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class User(AbstractBaseUser):
    """Define base user model for system"""
