import requests

def get_user_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
    data = {
        'country': response['country'],
        'region': response['region'],
        'city': response['city'],
        'timezone': response['timezone'],
        'latitude': response['loc'].split(',')[0],
        'longitude': response['loc'].split(',')[1]
    }

    return data