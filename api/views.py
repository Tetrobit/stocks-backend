""" Views """

import json
import requests
from django.http import HttpRequest, JsonResponse

from .models import Person

from .vkapi import account_get_profile_info

def index(_request: HttpRequest):
    """ Index endpoint """
    return JsonResponse({ 'ok': True })

def auth(request: HttpRequest):
    """ Auth user via VK """
    # requests.post()
    data = json.loads(request.body)
    response = account_get_profile_info(data['access_token'])['response']
    person_info = {
        'vk_id': response['id'],
        'first_name': response['first_name'],
        'last_name': response['last_name'],
        'photo': response['photo_200']
    }

    person = Person.objects.filter(vk_id=response['id'])
    if not person.exists():
        person = Person.objects.create(**person_info)
        person.save()
    else:
        person = person.first()

    return JsonResponse({ 'ok': True, 'response': person_info })

def check_auth(request: HttpRequest):
    """ Check auth """
    return JsonResponse({ 'ok': True, 'response': request.authorized })
