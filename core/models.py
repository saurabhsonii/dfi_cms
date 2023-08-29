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
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=350, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profile/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_role = models.CharField(choices=USER_ROLE, max_length=50)
    is_agent = models.BooleanField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
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


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    message = models.TextField()
    is_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class VehicleDetails(models.Model):
    parent_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=150)
    vehicle_name = models.CharField(max_length=150)
    vehicle_model = models.CharField(max_length=250)
    vehicle_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


TITLE = [
    ("mr", "MR"),
    ("mrs", "MRS"),
    ("other", "OTHER"),
]


class State(models.Model):
    state_name = models.CharField(max_length=150)
    state_code = models.CharField(max_length=150)


class PersonalDetails(models.Model):
    title = models.CharField(max_length=150, choices=TITLE)
    applicant_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    applicant_email = models.EmailField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=350)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    county = models.CharField(max_length=150, default="INDIA")
    vehicle_id = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OccupationDetails(models.Model):
    appcant = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class VehicleDocuments(models.Model):
    appcant = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    rc_card = models.FileField(upload_to="VehicleDocuments/")
    insurance = models.FileField(upload_to="VehicleDocuments/")
    form_29_30 = models.FileField(upload_to="VehicleDocuments/")
    form_34_35 = models.FileField(upload_to="VehicleDocuments/")
    bank_noc = models.FileField(upload_to="VehicleDocuments/")
    rto_noc = models.FileField(upload_to="VehicleDocuments/")
    form_28 = models.FileField(upload_to="VehicleDocuments/")
    created_at = models.DateTimeField(auto_now_add=True)


DURATION = [
    ("24 month", "24"),
    ("36 month", "36"),
    ("48 month", "48"),
    ("60 month", "60"),
]


class Disbrement(models.Model):
    bank_name = models.CharField(max_length=150)
    loan_amount = models.CharField(max_length=15)
    net_amount = models.CharField(max_length=15)
    emi_duration = models.CharField(max_length=50, choices=DURATION)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ApplicantDocuments(models.Model):
    appcant_id = models.ForeignKey(
        PersonalDetails, on_delete=models.CASCADE, null=True, blank=True)
    Occupation_id = models.ForeignKey(
        OccupationDetails, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=150)
    document_image = models.FileField(upload_to="applicant-details/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.document_name}"
