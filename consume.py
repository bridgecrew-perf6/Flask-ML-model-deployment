import requests


BASE_URL = 'http://127.0.0.1:5000/xor_predict'


x1 = str(input('Enter X1: '))
x2 = str(input('Enter X2: '))


URL = BASE_URL + "?x1=" + x1 + "&x2=" + x2


res = requests.get(URL)
if res.status_code==200:
    r = res.json()
    print(r['predicted_xor_value'])

