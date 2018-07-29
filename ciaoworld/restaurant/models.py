from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Custom auth user model representing a site administrator'''
    pass
