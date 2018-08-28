from django import forms
from django.contrib.auth.models import User
from BaseApp.models import UserInformation

class UserForm(forms.ModelForm):

#    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password','email')

class UserInformationForm(forms.ModelForm):

    class Meta:
        model = UserInformation
        fields = ('email','age','description','image')
