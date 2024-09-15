import configuration, data, requests

# Определение функции get_logs для проверки журналов сервера, в которой можно указать количество строк в ответе
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":5})

# Определяем функцию get_users_table для проверки, что пользователь успешно создан
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def get_kit_body(name):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

# Наборы ответов для промежуточных проверок функций
#response = get_logs()
#response = post_new_user(data.user_body)
response = get_users_table()
#response = post_products_kits(data.product_ids)

# Наборы для отображения промежуточных результатов функций
# Только коды ответа для любой функции
#print(response.status_code)

# Только заголовки ответа для любой функции
#print(response.headers)

# Для просмотра только токена из ответа при создании нового пользователя
#print(response.json()["authToken"])

# Для просмотра таблицы созданных пользователей
print(response.text)