from django.http import HttpRequest, JsonResponse

def index(_request: HttpRequest):
    return JsonResponse({ 'ok': True })

def auth(_request: HttpRequest):
    return JsonResponse({ 'ok': True })
