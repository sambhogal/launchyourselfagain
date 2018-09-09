from django.db import connection
from BaseApp.models import ModelDatabase
from django.core.cache import cache
from BaseApp.models import ModelDatabaseField
from django.utils import timezone
from BaseApp import models
from django.contrib.contenttypes.models import ContentType
import textwrap
import time


class ModelDBUtil():

    def createDynamicModel(self,tblName):
        print('*** createDynamicModel called with '+ '  --  ' + tblName)
        from django.db import models
        attrs = {
            '__module__':'BaseApp.models',
            'created' : models.DateTimeField(default=timezone.now()),
            'created_by' : models.CharField(blank=True,max_length=100),
            'number': models.CharField(blank=True,max_length=100),
            'updated':models.DateTimeField(blank=True),
            'updated_by':models.CharField(max_length=100),
            'rid':models.CharField(max_length=100),
        }
        # tblName = type(tblName,(models.Model,),attrs)
        str2 = tblName +'= type("'+tblName+'",(models.Model,),attrs)'
        exec(str2)
        print('***** Model created' + tblName)

    def tableDoesNotExit(self,tblName):
        self.tblName = tblName
        # OOB querySet??
        # with connection.cursor() as cursor:
        #     cursor.execute("create table {}(tutorial_id INT NOT NULL AUTO_INCREMENT,tutorial_title VARCHAR(100) NOT NULL,tutorial_author VARCHAR(40) NOT NULL,PRIMARY KEY ( tutorial_id ))".format(str_appName))

        mod_db_all = ModelDatabase.objects.all()
        print('All tables from ModelDatabase')
        self.table_flag = True
        for rec in mod_db_all:
            if rec.name == self.tblName:
                # print('Match Found for: ' + str(rec.name))
                self.table_flag = False
                break
            # else:
                # print('Match not found for this object ' + str(rec.name))

        return self.table_flag

    def createTableinDB(tblName):
        # str_appName = getAppName()
        str_app = ContentType.objects.get_for_model(ModelDatabase).app_label
        tblName = str_app.lower()+'_'+tblName.lower()

        with connection.cursor() as cursor:
            # SqlLite
            # cursor.execute("create table {}".format(str_appName))
            # MySQL
            # cursor.execute("create table {}(tutorial_id INT NOT NULL AUTO_INCREMENT,tutorial_title VARCHAR(100) NOT NULL,tutorial_author VARCHAR(40) NOT NULL,PRIMARY KEY ( tutorial_id ))".format(str_appName))
            def_fields_list =[]
            query = "create table {}({})".format(tblName,def_fields_list)
            cursor.execute(query)
            cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
            cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
            row = cursor.fetchone()
        return row

    def createModInFile(self,tblName):
        str_app ='testing'
        # This section is required for fields iteration
        f = 'created_sam = models.DateTimeField()\ncreated_by_sam = models.CharField(blank=True,max_length=100)\nnumber_sam = models.CharField(blank=True,max_length=100)'

        print('*** createDynamicModel called with '+ str_app + '  --  ' + tblName)
        tblName = 'Model'+tblName.capitalize()
        str_cls = """
class {}(models.Model):
    created = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(blank=True,max_length=100)
    number= models.CharField(blank=True,max_length=100)
    updated = models.DateTimeField(blank=True)
    updated_by=models.CharField(max_length=100)
    rid = models.CharField(max_length=100)
{}
    def __str__(self):
        return self.rid
        """.format(tblName,textwrap.indent(f,'    '))
        # str_app = str_app +'.models'
        # attrs = {
        #     '__module__':'BaseApp.models',
        #     'created' : models.DateTimeField(default=timezone.now()),
        #     'created_by' : models.CharField(blank=True),
        #     'number': models.CharField(blank=True),
        #     'updated':models.DateTimeField(blank=True),
        #     'updated_by':models.CharField(),
        #     'rid':models.CharField(),
        # }
        # tblName = type(tblName,(models.Model,),attrs)
        # str2 = tblName +'= type("'+tblName+'",(models.Model,),attrs)'
        # exec(str2)
        # print('content to write : '+str_cls)
        f = FileManager()
        # f.updateFile('tempfile2.py','a',str_cls)
        f.updateFile('BaseApp/models.py','a',str_cls)

        # Wait for 5 seconds
        #cache.clear()
        # exec('from django.db import models')
        # exec(str_cls)
        #app_cache.app_models[app_label][model_name.lower()]
        #cache.set('[BaseApp]['+tblName+']','')
        str5 = 'models.'+tblName
        #self.createDynamicModel(tblName)

        for x in cache:
            print(x[BaseApp])
        #f.readFile('BaseApp/models.py','r')
        print('***************** \n \n \n AFTER sleep code ')
        #with connection.schema_editor() as schema_editor:

            #schema_editor.create_model(exec(str5))
            #migration_executor = MigrationExecutor(schema_editor.connection)
            # migration_executor.apply_migration(ProLevel5())
        #
            # str6 = 'from BaseApp.models import '+ tblName
            # exec(str6)
            # try:
            #     from BaseApp import models
            #     schema_editor.create_model(exec(tblName))
            # except AttributeError:
            #     from BaseApp import models
            #     schema_editor.create_model(exec(tblName))
        print('***** Model created' + tblName)
        # f.readFile('BaseApp/models.py','r')
        # f.readFile('BaseApp/models.py','r')

class FileManager():

    def updateFile(self,filename,mod,content):

        file = open(filename,mod)
        file.writelines(content)
        file.close()
        # time.sleep(1)

    def readFile(self,filename,mod):
        file = open(filename,mod)
        #file.read()
        for line in file:
            print(line)
        file.close()
