import requests
from Dispenser import Dispenser

vr = {
    'name':'peaky-badger',
    'ingredients': [
            {
                'name': 'test',
                'measure': {
                    'unit': 'shots',
                    'amount':1
                }
            }
        ]
}


test_disp = {'name': 'test',
             'disp_type': 'optic',
             'index': 2,
             'remaining': {
                'unit': 'shots',
                'amount': 100
             }}


# menu = requests.post('http://10.11.12.41:5000/drinks', json=vr).json()
# menu = requests.get('http://10.11.12.41:5000/drinks', json=vr).json()
# menu = requests.get('http://10.11.12.41:5000/drinks/peaky-badger', json=vr).json()
#print(menu)

# menu = requests.post('http://10.11.12.41:5000/shutdown').json()
#menu = requests.post('http://10.11.12.41:5000/dispensers', json=test_disp).json()
# menu = requests.get('http://10.11.12.41:5000/dispensers').json()
# print(menu)

# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.post('http://10.11.12.41:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())

print(requests.post('http://10.11.12.41:5000/queue/peaky-badger').json())
