from django.contrib import admin
from BaseApp.models import School,Student,ModelDatabaseField,ModelDatabase
# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(ModelDatabase)
admin.site.register(ModelDatabaseField)
