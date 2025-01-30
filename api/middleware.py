from django.http import HttpRequest

from .utils.jwt import verifyJwt

class AuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        request.authorized = False

        access_token = request.COOKIES.get('access_token', None)

        if isinstance(access_token, str) and len(access_token) > 0:
            user_info = verifyJwt(access_token)
            print(user_info)
            if user_info:
                request.authorized = True
                request.user_id = user_info['id']

        response = self.get_response(request)
        return response
