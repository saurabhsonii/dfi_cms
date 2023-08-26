from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group as AuthGroup

# Create your models here.

#  users ---> login , register (user_roles -> admin, customers)

#  vichle ---> name, number, model

#  applicant -->

from django.contrib.auth.models import Permission

USER_ROLE = [
    ("agent", "AGENT"),
    ("manager", "MANAGER"),
]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=75)
    phone_number = models.PositiveIntegerField(max_length=12)
    address = models.CharField(max_length=350, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profile", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_role = models.CharField(choices=USER_ROLE, max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        AuthGroup,
        verbose_name=_('groups'),
        related_name='custom_user_groups',  # Unique related_name
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        related_name='custom_user_permissions',  # Unique related_name
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.email
