"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

number_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    lines = []
    with open("numbers.txt", "r") as file:
        for line in file:
            lines.append(' '.join(number_dict[word] if word in number_dict else word for word in line.split()) + '\n')
    with open("numbers_2.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
except IOError:
    print("Проблема с файлом")

