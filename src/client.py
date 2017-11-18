import requests

menu = requests.get('http://127.0.0.1:5000/menu').json()
print(menu)

# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/glass').json())
# print(requests.put('http://127.0.0.1:5000/queue/not-a-drink').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
# print(requests.put('http://127.0.0.1:5000/queue/Sex-on-the-Beach').json())
