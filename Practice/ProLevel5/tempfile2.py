from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def createTableinDB(str_appName):
    # str_appName = getAppName()
    from django.db import connection
    with connection.cursor() as cursor:
        # SqlLite
        cursor.execute("create table {}".format(str_appName))
        # MySQL
        # cursor.execute("create table {}(tutorial_id INT NOT NULL AUTO_INCREMENT,tutorial_title VARCHAR(100) NOT NULL,tutorial_author VARCHAR(40) NOT NULL,PRIMARY KEY ( tutorial_id ))".format(str_appName))
        # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row

def createDynamicModel(str_app,tblName):
    print('*** createDynamicModel called with '+ str_app + '  --  ' + tblName)
    from django.db import models
    tblName = 'Model'+tblName.capitalize()
    # tblName = str_app+'_'+tblName
    str_app = str_app +'.models'
    attrs = {
        '__module__':'BaseApp.models',
        'created' : models.DateTimeField(default=timezone.now()),
        'created_by' : models.CharField(blank=True),
        'number': models.CharField(blank=True),
        'updated':models.DateTimeField(blank=True),
        'updated_by':models.CharField(),
        'rid':models.CharField(),
    }
    # tblName = type(tblName,(models.Model,),attrs)
    str2 = tblName +'= type("'+tblName+'",(models.Model,),attrs)'
    exec(str2)
    print('***** Model created' + tblName)


def createModelDatabase2(request):
    if request.method == "POST":
        mod_db_form = ModelDatabaseForm(data=request.POST)

        if mod_db_form.is_valid():
            mod_db = mod_db_form.save()
            from django.urls import resolve
            # createDynamicModel(str(resolve(request.path_info).app_name),mod_db.name)
            # createTableinDB(str(resolve(request.path_info).app_name) +'_'+ mod_db.name)
        else:
            print(mod_db_form.errors)

        return HttpResponse('Model Tabel created!!')
        #return HttpResponseRedirect(reverse('login_url'))
    else:
        mod_db_form = ModelDatabaseForm()

        form = {'mod_db_form':mod_db_form}

        return render (request,'BaseApp/modeldatabase_form.html',context=form)


class ModelTable3(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    def __str__(self):
        return self.rid

#start_model_ModelTable4
class ModelTable4(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    def __str__(self):
        return self.rid
#start_model_ModelTable4

class ModelTbl10(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA10(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA11(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA12(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA13(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA14(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA15(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA16(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelNone(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA17(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA18(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA19(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelDf123(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelDf1235(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        
class ModelA21(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True)
    number= models.CharField(blank=True)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField()
    rid = models.CharField()
    created_sam = models.DateTimeField(default=timezone.now())
	created_by_sam = models.CharField(blank=True)
	number_sam = models.CharField(blank=True)
    def __str__(self):
        return self.rid
        