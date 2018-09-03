#from django.utils.deprecation import MiddlewareMixin

class CreateDBObject(object):
    def __init__(self,get_response):
        print('INIT')
        self.get_response = get_response

    def __call__(self, request):
        print("IN CALL FUNCTION")
        response = self.get_response(request)

        print("IN CALL FUNCTION 222222222222222222\n")
        print(response.status_code)
        ###Code below is not working -- seems like process_response is deprecated?
        def process_response(request,response):
            print("*****IN Process Response")

        return response
