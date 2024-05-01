from django.db import models
from django.contrib.auth.models import AbstractUser


class RentOwner(AbstractUser):
    renting_now = models.BooleanField(default=False)