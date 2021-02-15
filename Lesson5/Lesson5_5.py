"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран."""

try:
    with open("numbers_count.txt", "w", encoding="utf-8") as file:
        line = input("Введите цифры через пробел: ")
        file.writelines(line)
        numbers = line.split()
        print(f"Сумма чисел: {sum(map(int, numbers))}")
except IOError:
    print("Проблема с файлом")


