"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке. """

try:
    with open("counter.txt", "r") as file:
        lines = file.readlines()
        print(f"Всего строк: {len(lines)}")
        for i in range(len(lines)):
            print(f"{i + 1} строка: {len(lines[i].split())} слов")
except IOError:
    print("Проблема с файлом")
