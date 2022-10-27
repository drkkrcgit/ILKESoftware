"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, username, user_group, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not username:
            raise ValueError('User must have a username.')
        if 'is_superuser' in extra_fields:
            user_group = ""
        elif not user_group:
            raise ValueError('User must have a user group.')
        user = self.model(
            username=username,
            user_group=user_group,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, user_group=None):
        """Create and return a new superuser."""
        user = self.create_user(username,
                                user_group,
                                password,
                                is_superuser=True)
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    username = models.CharField(max_length=30, unique=True)
    user_group = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
