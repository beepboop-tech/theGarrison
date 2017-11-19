import requests

menu = requests.get('http://10.11.12.41:5000/dispensers').json()
print(menu)

# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
