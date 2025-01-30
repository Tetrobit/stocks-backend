import requests

base_url = 'https://api.vk.com/method/'

def account_get_profile_info(access_token):
    url = base_url + 'account.getProfileInfo'
    params = {
        'access_token': access_token,
        'v': '5.199'
    }
    return requests.get(url, params=params, timeout=5).json()
