""" Views """

import json
import requests
from django.http import HttpRequest, JsonResponse

from .vkapi import account_get_profile_info

def index(_request: HttpRequest):
    """ Index endpoint """
    return JsonResponse({ 'ok': True })

def auth(request: HttpRequest):
    """ Auth user via VK """
    # requests.post()
    data = json.loads(request.body)
    user_info = account_get_profile_info(data['access_token'])['response']
    return JsonResponse({ 'ok': True, 'response': user_info })

def check_auth(request: HttpRequest):
    """ Check auth """
    return JsonResponse({ 'ok': True, 'response': request.authorized })
