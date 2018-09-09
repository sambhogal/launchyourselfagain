from django.urls import path,re_path
from BaseApp import views

app_name = 'base_app'

urlpatterns = [
    re_path(r'^register/',views.register_user,name='register_url'),
    re_path(r'^login/',views.login_user,name='login_url'),
    re_path(r'^logout/',views.logout_user,name='logout_url'),
    re_path(r'^class_based_view/',views.ClassBasedView.as_view(),name='class_based_view_url'),
    re_path(r'^class_based_template_view',views.ClassBasedTemplateView.as_view(),name='class_based_template_view_url'),
    re_path(r'^create_school',views.CreateSchool.as_view(),name='create_school_url'),
    re_path(r'^create_student',views.CreateStudent.as_view(),name='create_student_url'),

    # re_path(r'^modeldatabase/',views.CreateModelDatabase.as_view(),name='create_modeldb_url'),
    re_path(r'^modeldatabase/',views.CreateModelDatabase.as_view(),name='create_modeldb_url'),
    re_path(r'^modeldatabasefields/',views.CreateModelDatabaseFields.as_view(),name='create_modeldb_fields_url'),
]
