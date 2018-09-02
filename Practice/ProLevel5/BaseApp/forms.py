from django import forms
from django.contrib.auth.models import User
from BaseApp.models import UserInformation, ModelDatabase

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')

class UserInformationForm(forms.ModelForm):

    class Meta:
        model = UserInformation
        fields = ('age','description','image')

class ModelDatabaseForm(forms.ModelForm):

    class Meta:
        model = ModelDatabase
        fields = ('label','name')
