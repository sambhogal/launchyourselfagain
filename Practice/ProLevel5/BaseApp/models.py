from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserInformation(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True)
    image = models.ImageField(upload_to='profile_pics',blank=True)
    description = models.CharField(max_length=250)


    def __str__(self):
        return self.user.username

class School(models.Model):

    school_name = models.CharField(max_length=250,blank=True)
    school_location = models.CharField(max_length=250,blank=True)
    principal = models.CharField(max_length=100,blank=True)
    school_email = models.EmailField(blank=True)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        return reverse('base_app:login_url')  #To be updated when we have a view

class Student(models.Model):

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICES = (
                    (MALE, 'Male'),
                    (FEMALE, 'Female'),
                    )

    student_name = models.CharField(max_length=100,blank=True)
    student_age = models.PositiveIntegerField(blank=True)
    student_gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('base_app:login_url')  #To be updated when we have a view
