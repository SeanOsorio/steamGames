import requests
url="https://ipinfo.io/190.60.194.144/json"
try:
    response = requests.get(url)
    data = requests.json()
    print(data)

except:
    print("hubo un error")