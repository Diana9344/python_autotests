import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b5fe78f88dcd208ebf061b1862ac2eb0"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = '4263'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID}, headers={"Accept": "application/json"})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('status_code', '200'), ('reason', 'OK')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.status_code == 200
    assert response_parametrize.reason == "OK"

@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', 'Диана')])
def test_parametrize_two(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}, headers={"Accept": "application/json"})
    assert response_parametrize.json()["data"][0][key] == value
