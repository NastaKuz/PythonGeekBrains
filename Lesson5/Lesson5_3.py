"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников. """

try:
    with open("employees.txt", encoding="utf-8") as file:
        salary_sum = 0
        lines = file.readlines()
        for line in lines:
            surname, salary = line.split()
            salary_sum += int(salary)
            if int(salary) < 20000:
                print(surname)
        print(f"Средний доход сторудников: {salary_sum/len(lines)}")
except IOError:
    print("Проблема с файлом")
except ValueError:
    print("Неверный формат данных")

