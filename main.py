import requests

# кладем все данные которые вернуться после запроса
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# из переменой респонс мы обращаемся  к хистори, это массив в котором хранится информация о всех запросах
#Мы выбираем первую переменну массива и кладем ее с переменную first_response
first_response = response.history[0]
#перекладываем информацию с переменной response в second_response
second_response = response

print(first_response.url)
print(second_response.url)

