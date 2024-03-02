import requests


API_KEY = 'VP3WYKFZZstl1xE8bscxv6Qpxns4fgxsN9vyvn527UbAVzpPiB'
SECRET_KEY = 'hdLDJEBDQtjvvqpdS9tZSrfqHXMU85BVXkWWqkBN'


def get_random_pet(oath):
    resp = requests.get(
        'https://api.petfinder.com/v2/animals?limit=100',
        headers={"Authorization": f"Bearer {oath}"}
    )

    #TODO:


def get_oath_token():
    resp = requests.post(
        'https://api.petfinder.com/v2/oauth2/token',
        data={'grant_type': 'client_credentials',
                'client_id': API_KEY,
                'client_secret': SECRET_KEY}
    )

    return resp.json()['access_token']
