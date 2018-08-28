from django.shortcuts import render
from BaseApp.forms import UserInformationForm,UserForm

# Create your views here.
def index(request):
    return render (request,'BaseApp/index.html')

def login(request):
    user_form = UserForm()
    user_info_form = UserInformationForm()

    form = {'user_form':user_form,'user_info_form':user_info_form}

    return render (request,'BaseApp/register.html',context=form)
