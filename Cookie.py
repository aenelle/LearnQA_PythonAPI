import requests
payload = {"login":"secret_login", "password":"secret_pass"} # готовим данные
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload) # передаем их в data

cookie_value = response1.cookies.get('auth_cookie') # из переменной response1  с помощью get  получаем куки со значением auth_cookie и кладем ее в переменную cookie_value

cookies = {'auth_cookie': cookie_value} # подготавливаем второй запрос, создаем словарь для авторизованной куки  и делем сам запрос
cookies = {} # создали массив и убедились что куки не являются None и только в этом случае мы ее добавляем в переменную функц.update
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

# результат кладем в переменную response2



response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)



#print(response.text)
#print(response.status_code)
#print(dict(response.cookies)) # dikt привести к словарю а не объект

#print(response.headers)

