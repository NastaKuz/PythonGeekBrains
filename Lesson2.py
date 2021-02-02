def first():
    my_list = [1, '1', 'hello', (1, 2), [1, 2], True, 6.5]
    for i in my_list:
        print(f"{i}: тип {type(i)}")


def second():
    my_list = []
    n = input("Задайте размер списка: ")
    if n.isdigit():
        n = int(n)
        for _ in range(n):
            my_list.append(input())
        for i in range(1, len(my_list), 2):
            my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
        for i in range(len(my_list)):
            print(my_list[i])
    else:
        print("Введено не число")


def third():
    month = input("Введите номер месяца: ")
    my_list = [
        ['Зима', [1, 2, 12]],
        ['Весна', [3, 4, 5]],
        ['Лето', [6, 7, 8]],
        ['Осень', [9, 10, 11]]
    ]
    my_dict = {
        "Зима": (1, 2, 12),
        "Весна": (3, 4, 5),
        "Лето": (6, 7, 8),
        "Осень": (9, 10, 11),
    }
    if month.isdigit():
        month = int(month)
        if 0 < month < 13:
            for key, value in my_dict.items():
                if month in value:
                    print(f"По словарю {month} месяц это {key}")
            for key, value in my_list:
                if month in value:
                    print(f"По списку {month} месяц это {key}")
        else:
            print("Такого месяца не существует")
    else:
        print("Неверный ввод данных")


def forth():
    my_string = input("Введите строку")
    for idx, item in enumerate(my_string.split()):
        print(idx + 1, ":", item[:10])


def fifth():
    rating = [8, 7, 3, 3, 2, 1]
    user_number = input("Введите новый рейтинг")
    if user_number.isdigit():
        user_number = int(user_number)
        position = len(rating)
        for idx, number in enumerate(rating):
            if user_number > number:
                position = idx
                break
        rating.insert(position, user_number)
        print(position)
    else:
        print("Неверные данные")
    print(rating)


def sixth():
    goods = []
    features = ["name", "amount", "price", "units"]
    while input("Добавить новый товар? (y)") == 'y':
        new_dict = {}
        for i in features:
            feature = input(f"Введите значение {i}: ")
            new_dict[i] = int(feature) if feature.isdigit() else feature
        goods.append(tuple((len(goods), new_dict)))
    print(goods)
    if input("Показать аналитику? (y)") == 'y':
        analytics_dict = {}
        for good in goods:
            for key, value in good[1].items():
                if key in analytics_dict:
                    analytics_dict[key].append(value)
                else:
                    analytics_dict[key] = [value]
        print(analytics_dict)


# first()
# second()
# third()
# forth()
# fifth()
# sixth()
