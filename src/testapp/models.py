from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True),
    phone = models.CharField(null=True, max_length=255),
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'user_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
