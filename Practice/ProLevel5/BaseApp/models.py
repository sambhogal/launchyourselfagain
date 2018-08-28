from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInformation(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.CharField(max_length=250)


    def __str__(self):
        return self.user.username
