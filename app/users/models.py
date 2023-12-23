from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass



class Dbase(models.Model):
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    def __str__(self) -> str:
        return 'User - {0}, Text - {1}, Complete - {2}'.format(self.user, self.text, self.complete)
    