from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                PermissionsMixin
from datetime import datetime


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('This object requires an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics/% Y/% m/% d/')
    registration_date = models.DateTimeField(default=datetime.now())
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Comments(models.Model):
    date_created = models.DateTimeField(default=datetime.now())
    comment_content = models.CharField(max_length = 400)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)