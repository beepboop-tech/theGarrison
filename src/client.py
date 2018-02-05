import requests
# from Dispenser import Dispenser

d = {
    'name':'gin',
    'ingredients': [
            {
                'name': 'gin',
                'measure': {
                    'unit': 'shots',
                    'amount':1
                }
            }

        ]
}




gin = {'name': 'gin',
             'disp_type': 'optic',
             'index': 0,
             'remaining': {
                'unit': 'shots',
                'amount': 40
             }
        }

amo = {'name': 'amo',
          'disp_type': 'optic',
          'index': 2,
          'remaining': {
             'unit': 'shots',
             'amount': 20
          }}

rum = {'name': 'rum',
          'disp_type': 'optic',
          'index': 7,
          'remaining': {
             'unit': 'shots',
             'amount': 30
          }}



# menu = requests.post('http://10.11.12.41:5000/drinks', json=vr).json()
# menu = requests.get('http://10.11.12.41:5000/drinks', json=d).json()
menu = requests.post('http://10.11.12.41:5000/queue/gin').json()

# menu = requests.post('http://10.11.12.41:5000/shutdown').json()
# menu = requests.get('http://10.11.12.41:5000/dispensers', json=rum).json()
# menu = requests.post('http://10.11.12.41:5000/dispensers', json=gin).json()
# print(menu)

# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.post('http://10.11.12.41:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())

# print(requests.post('http://10.11.12.41:5000/queue/sex-on-the-beach').json())
