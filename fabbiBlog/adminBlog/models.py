from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
import random
import adminBlog.constants as _const
from django.conf import settings


class myUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        color = random.choice(_const.AVA_COLORS)
        return self._create_user(email, username, password, color_avatar=color, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        color = random.choice(_const.AVA_COLORS)
        return self._create_user(email, username, password, color_avatar=color, **extra_fields)


# Create your models here.
class myUser(AbstractUser):
    email = models.EmailField(blank=True, null=True, max_length=255, unique=True)
    username = models.CharField(blank=True, null=True, max_length=255, unique=False)
    color_avatar = models.CharField(blank=True, null=True, max_length=255, unique=False)
    device_id = models.CharField(blank=True, null=True, max_length=255)
    is_baned = models.BooleanField(default=False)

    objects = myUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'tbl_myuser'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email


class UserProfile(models.Model):
    GENDERS = (
        (_const.OTHER, _const.OTHER),
        (_const.MALE, _const.MALE),
        (_const.FEMALE, _const.FEMALE)
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='userProfile', blank=True)
    gender = models.CharField(max_length=20, choices=GENDERS, default=_const.OTHER)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'tbl_user_profile'

    def __str__(self):
        return str(self.user)
