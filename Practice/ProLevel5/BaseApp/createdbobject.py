#from django.utils.deprecation import MiddlewareMixin

class CreateDBObject(object):
    def __init__(self,get_response):
        print('INIT')
        self.get_response = get_response

    def __call__(self, request):
        print("IN CALL FUNCTION")
        print("Request attributes : "+ str(request.method))
        # print("Request attributes : "+ str(request.current_app))
        # print("Request attributes : "+ str(request.urlconf))
        # print("Request attributes : "+ str(request.site))
        print("Request attributes : "+ str(request.get_host()))
        print("Request username : "+ str(request.POST.get('username')))
        print(list(request.POST.items()))
        print('For loop start')
        for x in request.POST.items():
            print(x)
        print("Request attributes : "+ str(request.path_info))
        # print("Request body : "+ str(request.body))
        response = self.get_response(request)
        #   print('What is response '+ str(response.content))
        print("IN CALL FUNCTION 222222222222222222\n")
        print(response.status_code)
        ###Code below is not working -- seems like process_response is deprecated?
        def process_response(request,response):
            print("*****IN Process Response")

        return response
