import requests

vr = {
    'name':'double-vodka-and-rum',
    'ingredients': ['vodka', 'vodka', 'rum']
}


menu = requests.get('http://10.11.12.41:5000/drinks', json=vr).json()
print(menu)
menu = requests.put('http://10.11.12.41:5000/shutdown', json=vr).json()


# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
