#from django.utils.deprecation import MiddlewareMixin
from BaseApp.utils import ModelDBUtil
from django.conf import settings

class CreateDBObject(object):
    def __init__(self,get_response):
        print('INIT')
        self.get_response = get_response

    def isModReqTblCreation(self,request):
        print('***custom FUNCTION called')
        req_path = request.path_info.split('?')
        #FUTURE - Include the logic to run the middleware on operations
        #FUTURE - Include the logic to run on query as well
        for mod in settings.RUN_MIDDLEWARE:
            if req_path[0].endswith('/'+mod['NAME']+'/') or req_path[0].endswith('/'+mod['NAME']):
                print('Model name is : '+ mod['NAME'])
                try:
                    if mod['METHOD'] != '' and request.method != mod['METHOD']:
                        return False
                    else:
                        return True
                except IOError:
                    print('Key is not define in RUN_MIDDLEWARE dictionary')
                return True
        return False

    def __call__(self,request):
        print("Befoe View called --------- IN Middleware")
        # print("Request attributes : "+ str(request.method))
        # print("Request app name : "+ str(request.current_app))
        # # print("Request attributes : "+ str(request.urlconf))
        # # print("Request attributes : "+ str(request.site))
        # print("Request attributes : "+ str(request.get_host()))
        # print("Request username : "+ str(request.POST.get('username')))
        # print(list(request.POST.items()))
        # print('For loop start')
        # for x in request.POST.items():
        #     print(x)
        print("Request attributes : "+ str(request.path_info))
        # # print("Request body : "+ str(request.body))
        # print("After View Called --------\n")
        #need to check path if create tablenct
        #need to create a properly file for Constants
        run_mid = self.isModReqTblCreation(request)
        # check if middleware required to run
        if run_mid:
            db_obj = ModelDBUtil()
            tableDoesNotExist = db_obj.tableDoesNotExit(str(request.POST.get('name')))

            print('********'+ str(tableDoesNotExist))

        response = self.get_response(request)
        # print('What is response '+ str(response.content))
        # if tableDoesNotExist


        print(response.status_code)
        # ###Code below is not working -- seems like process_response is deprecated?
        # def process_response(request,response):
        #     print("*****IN Process Response")
        return response
