import requests
from xml.etree import ElementTree

def get_current_course():
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    root = ElementTree.fromstring(response.text)

    result = dict()
    for valute in root:
        val_id = valute.get('ID')
        code = valute.find('CharCode').text
        value = valute.find('VunitRate').text.replace(',', '.')
        name = valute.find('Name').text
        result[code] = { 'name': name, 'value': value, 'val_id': val_id }

    return result

def get_dynamic(date_req1, date_req2, val_id):
    params = {
        'date_req1': date_req1,
        'date_req2': date_req2,
        'VAL_NM_RQ': val_id
    }

    response = requests.get('https://www.cbr.ru/scripts/XML_dynamic.asp', params=params)
    root = ElementTree.fromstring(response.text)
    result = []
    for record in root:
        date = record.get('Date')
        value = record.find('VunitRate').text.replace(',', '.')
        result.append([date, value])
    return result
