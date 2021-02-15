"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб). Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
import re

subject_dict = {}

try:
    with open("subjects.txt", "r", encoding="utf-8") as file:
        for line in file:
            sum_hours = 0
            subject_name, subject_hours = line.split()[0].strip(":"), line.split()[1:]
            hours = [''.join(re.findall("(\d+)", item)) for item in subject_hours]
            sum_hours = sum([int(item) if item.isdigit() else 0 for item in hours])
            subject_dict[subject_name] = sum_hours
    print(subject_dict)
except IOError:
    print("Проблема с файлом")
