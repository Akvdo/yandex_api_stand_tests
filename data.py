# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания новой записи пользователя в системе
# содержат имя, телефон и адрес пользователя
user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+74441237887",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Хохотушкина, д. 16"  # Адрес пользователя
}

product_ids = {
    "ids":[1,2,3]
}