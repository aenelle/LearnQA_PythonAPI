import requests

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

responseEX4 = requests.get("https://playground.learnqa.ru/api/get_text")
print(responseEX4.text)
