""" Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список
сохранить в виде json-объекта в соответствующий файл. Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
"firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json

profit_dict = {}
avg_dict = {}

list_to_JSON = [profit_dict, avg_dict]

avg_sum = []

try:
    with open("firms.txt", "r", encoding="utf-8") as file:
        for line in file:
            firm_name, firm_type, revenue, loss = line.split()
            profit = int(revenue) - int(loss)
            profit_dict[firm_name] = profit
            if profit > 0:
                avg_sum.append(profit)
    avg_dict["average_profit"] = sum(avg_sum)/len(avg_sum)
    print(list_to_JSON)

    with open("firms.json", "w") as json_file:
        json.dump(list_to_JSON, json_file)

except IOError:
    print("Проблема с файлом")
