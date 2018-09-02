from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#Create your models here.
class ModelDatabase(models.Model):

    label = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True)

    def get_absolute_url(self):
        return reverse('base_app:create_modeldb_fields_url')

    def __str__(self):
        return self.name


class ModelDatabaseField(models.Model):
    # from BaseApp.views import ModelDatabase
    CHAR_FIELD = 'models.CharField(max_length=200,blank=True)'
    TEXT_AREA = 'models.TextField(max_length=1000,blank=True)'
    BOOLEAN_FIELD = 'model.BooleanField()'
    DATE_TIME = 'models.DateTimeField()'

    ATTRIBUTE_CHOICES = (
                        (CHAR_FIELD,'Character Field'),
                        (TEXT_AREA,'Text Area Field'),
                        (BOOLEAN_FIELD,'Boolean Field'),
                        (DATE_TIME,'Date Time Field'),
                        )

    model_database = models.ForeignKey(ModelDatabase,on_delete=models.CASCADE)
    label = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True)
    type = models.CharField(max_length=100,choices=ATTRIBUTE_CHOICES)

    def get_absolute_url(self):
        return reverse('index_url')

    def __str__(self):
        return self.name

class ModelView(models.Model):
    view_name = models.CharField(max_length=50)
    model_database = models.ForeignKey(ModelDatabase,on_delete=models.CASCADE)
#    type = ['View','CreateView','UpdateView','DetailView','ListView','TemplateView']
    type = models.CharField(max_length=20,blank=True)
    view_code = models.TextField()

    def __str__(self):
        return self.view_name

class ModelURL(models.Model):
    url_name =  models.CharField(max_length=50)
    url_encoded = models.TextField()
    url_view = models.ForeignKey(ModelView,on_delete=models.CASCADE)

    def __str__(self):
        return self.url_name

class ModelCode(models.Model):
    model_code_name = models.CharField(max_length=20)
    model_database = models.ForeignKey(ModelDatabase,on_delete=models.CASCADE)
    model_code = models.TextField()

    def __str__(self):
        return self.model_code_name


#######################################################PREVIOUS EXERCISES##############################################

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
