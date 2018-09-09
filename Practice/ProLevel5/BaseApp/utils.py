from django.db import connection
from BaseApp.models import ModelDatabase
from BaseApp.models import ModelDatabaseField

class ModelDBUtil():

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
                print('Match Found for: ' + str(rec.name))
                self.table_flag = False
                break
            else:
                print('Match not found for this object ' + str(rec.name))

        return self.table_flag
