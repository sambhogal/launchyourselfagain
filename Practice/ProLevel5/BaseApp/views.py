from django.shortcuts import render
from BaseApp.forms import UserInformationForm,UserForm,ModelDatabaseForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,TemplateView,CreateView
from BaseApp.models import School,Student,ModelDatabaseField,ModelDatabase

from django.utils import timezone
from django.urls import resolve

#from django.db import models
# form django.
# Create your views here.

###TO DO:
#  Create UpdateView and ListView views for platform static classes

class CreateModelDatabase(CreateView):
    fields = ('label','name')
    model = ModelDatabase
    # 1. Get recent created name & id from ModelDatabase
    # 2. Get all fiels from ModelDatabaseFileds where id = pk_id
    #print(self.request.method)
    #def x(self):
        #print('****************************************************\n')
        #print(self.request.method)

#createTableinDB('BaseApp_incident2')

class CreateModelDatabaseFields(CreateView):
    fields = ('model_database','label','name','type')
    model = ModelDatabaseField



###################################OLD EXERCISES############################

class CreateSchool(CreateView):
    fields = ('school_name','school_location','principal','school_email')
    model = School
    # print('\n\n')
    # def getData(self):
    #     print(self.request)


class CreateStudent(CreateView):
    fields = ('school','student_name','student_age','student_gender')
    model = Student

    print('*****Student created and activate middleware ')




class ClassBasedView(View):
    def get(self,request):
        return HttpResponse("Class based View called")

class index(TemplateView):
    template_name = 'BaseApp/index.html'

class ClassBasedTemplateView(TemplateView):
    template_name = 'BaseApp/classbasedview.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = 'Sam'
        context['last_name'] = 'Bhogal'
        return context

# def index(request):
#     return render (request,'BaseApp/index.html')

def register_user(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInformationForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_info_form.save(commit=False)
            profile.user = user #remember that we need to set the reference when updating multiple tables

            if 'profile_pic' in request.FILES:
                print('Found a picture')
                profile.image = request.FILES['profile_pic']
            print('******CODE WAS HERE')
            profile.save()
        else:
            print(user_form.errors,user_info_form.errors)
        return HttpResponse('You are registered, Please login')
        #return HttpResponseRedirect(reverse('login_url'))

    else:
        user_form = UserForm()
        user_info_form = UserInformationForm()
        form = {'user_form':user_form,'user_info_form':user_info_form}

        return render (request,'BaseApp/register.html',context=form)

def login_user(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index_url'))
                else:
                    return HttpResponse('Account is not active')
            else:
                print("User tried to login with: \n Username: {} \n Password: {} ".format(username,password))
                return render(request,'BaseApp/login.html')

        else:
            return render(request,'BaseApp/login.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_url'))
