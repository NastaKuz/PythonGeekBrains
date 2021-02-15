"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка. """

line_list = []
line = input("Введите текст, для окончания работы введите пустую строку: ")

while line:
    line_list.append(line + '\n')
    line = input()

try:
    with open("new_text.txt", "w") as file:
        file.writelines(line_list)
except IOError:
    print("Проблема с файлом")
