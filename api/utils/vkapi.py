import os
import requests

base_url = 'https://api.vk.com/method/'

def get_access_token(auth_data):
    url = 'https://id.vk.com/oauth2/auth'
    params = {
        'redirect_uri': auth_data['redirect_uri'],
        'state': auth_data['state'],
        'client_id': os.environ['VK_APP_ID'],
        'grant_type': 'authorization_code',
        'code_verifier': auth_data['code_verifier'],
        'device_id': auth_data['device_id'],
    }

    request_data = {
        'code': auth_data['code'],
    }

    return requests.post(url, params=params, data=request_data, timeout=5).json()['access_token']


def account_get_profile_info(access_token):
    url = base_url + 'account.getProfileInfo'
    params = {
        'access_token': access_token,
        'v': '5.199'
    }
    return requests.get(url, params=params, timeout=5).json()
