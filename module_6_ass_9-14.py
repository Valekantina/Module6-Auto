# Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.
# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.

def is_equal_string(utf8_string, utf16_string):
    first = utf8_string.decode('utf8')
    second = utf16_string.decode('utf16')
    a = first.casefold()
    b = second.casefold()
    if a == b:
        return True
    else:
        return False

        