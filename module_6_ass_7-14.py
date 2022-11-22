#Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.
#Вимоги:
#прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
#запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
#запис нового вмісту файлу output має бути одноразовий і використовувати метод write

def sanitize_file(source, output):
    with open(source, 'r') as reader:
        with open(output,'w') as writer:
            read = reader.read()
            sanit_read = read.strip().replace('0', '').replace('1', '').replace('2', '').replace('3', '') \
        .replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
            writer.write(sanit_read)
            
            