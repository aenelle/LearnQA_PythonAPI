import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
responses = response.history
count = len(responses)
print(f"Количество редиректов {count}")

second_response = response.history[1]
print(second_response.url)
