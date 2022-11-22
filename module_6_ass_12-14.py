# Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:
#['andry:uyro18890D', 'steve:oppjM13LL9e']
#Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:
#['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

import base64

def encode_data_to_base64(data):
    file = []
    for i in data:
        info = i.encode("utf8")
        list = base64.b64encode(info)
        list_clean = list.decode("utf8")
        file.append(list_clean)
    return file

    