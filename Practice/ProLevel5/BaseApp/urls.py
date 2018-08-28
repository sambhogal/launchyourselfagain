from django.urls import path,re_path
from BaseApp import views

app_name = 'base_app'

urlpatterns = [
    re_path(r'^register/',views.login,name='register_url'),
]
