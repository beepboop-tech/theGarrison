import requests
from Dispenser import Dispenser

vr = {
    'name':'peaky-badger',
    'ingredients': ['vodka', 'gin']
}


# menu = requests.get('http://10.11.12.41:5000/drinks', json=vr).json()
# menu = requests.get('http://10.11.12.41:5000/drinks/peaky-badger', json=vr).json()
# print(menu)

j = {'name': 'test', 'index': 1, 'remaining': 100}

menu = requests.post('http://10.11.12.41:5000/shutdown').json()
# menu = requests.get('http://10.11.12.41:5000/dispensers', json=j).json()
print(menu)

# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
