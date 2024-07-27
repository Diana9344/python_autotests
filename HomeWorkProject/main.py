import requests

HOST = 'https://api.pokemonbattle.ru'
token = 'b5fe78f88dcd208ebf061b1862ac2eb0'
pokemon_id = '29812'

# Запрос на создание покемона
response = requests.post(url=f'{HOST}/v2/pokemons', json={
                        'name': 'Бульбазавр',
                        'photo_id': '003'
                        },
                        headers={'Content-Type': 'application/json',
                                 'trainer_token': f'{token}'})

print(response.status_code, response.reason, response.text)

# Запрос на изменение имени покемона
response = requests.put(url=f'{HOST}/v2/pokemons', json={
                        'pokemon_id': f'{pokemon_id}',
                        'name': 'Onion',
                        'photo_id': '003'
                        },
                        headers={'Content-Type': 'application/json',
                                 'trainer_token': f'{token}'})

print(response.status_code, response.reason, response.text)

# Запрос на добавление покемона в покебол
response = requests.post(url=f'{HOST}/v2/trainers/add_pokeball', json={
                        'pokemon_id': f'{pokemon_id}'
                        },
                        headers={'Content-Type': 'application/json',
                                 'trainer_token': f'{token}'})

print(response.status_code, response.reason, response.text)