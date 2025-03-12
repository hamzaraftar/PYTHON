# function base Middleware

# def my_middlewares(get_response):
#     print('One time initialization')

#     def my_function(request):
#         print('This is before view')
#         response = get_response(request)
#         print('This is after view')
#         return response
#     return my_function

# Class base Middleware

class my_middlewares:
    def __init__(self,get_response):
        self.get_response = get_response
        print('One time initialization')

        def __call__(self,request):
            print('This is before view')
            response = self.get_response(request)
            print('This is after view')
            return response