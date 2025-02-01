""" Views """

import json
import re

from django.conf import settings
from django.http import HttpRequest, JsonResponse, HttpResponse

from .models import Person

from .utils.cbr import get_current_course, get_dynamic
from .utils.jwt import generateJwt
from .utils.vkapi import account_get_profile_info, get_access_token

def index(_request: HttpRequest):
    """ Index endpoint """
    return JsonResponse({ 'ok': True })

def auth(request: HttpRequest):
    """ Auth user via VK """

    data = json.loads(request.body)
    access_token = get_access_token(data)
    response = account_get_profile_info(access_token)['response']

    person_info = {
        'vk_id': response['id'],
        'first_name': response['first_name'],
        'last_name': response['last_name'],
        'photo': response['photo_200'],
    }

    person = Person.objects.filter(vk_id=response['id'])
    if not person.exists():
        person = Person.objects.create(**person_info)
        person.save()
    else:
        person = person.first()

    person_info['id'] = person.id

    response = JsonResponse({
        'ok': True, 
        'response': person_info,
    })

    jwt = generateJwt({
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'photo': person.photo,
    })

    if settings.DEBUG:
        response.set_cookie('access_token', jwt)
    else:
        response.set_cookie('access_token', jwt, samesite='none', secure=True)

    return response

def check_auth(request: HttpRequest):
    """ Check auth """
    if not request.authorized:
        return JsonResponse({ 'ok': False })
    
    try:
        person = Person.objects.get(pk=request.user_id)
    except:
        return JsonResponse({ 'ok': False })

    return JsonResponse({ 'ok': True, 'response': {
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'photo': person.photo,
    }})

def logout(_request: HttpRequest):
    """ Logout user """
    response = JsonResponse({ 'ok': True })
    if settings.DEBUG:
        response.set_cookie('access_token', '')
    else:
        response.set_cookie('access_token', '', samesite='none', secure=True)
    return response

def daily_course(_request: HttpRequest):
    """ Get course of the certain day """

    return JsonResponse({ 'ok': True, 'response': get_current_course() })

def dynamic_course(request: HttpRequest):
    """ Get course of the certain day """
    date_req1 = request.GET.get('date_req1')
    date_req2 = request.GET.get('date_req2')
    val_id = request.GET.get('val_id')

    return JsonResponse({
        'ok': True,
        'response': get_dynamic(date_req1, date_req2, val_id)
    })
