def first():
    number = 5
    color = "красный"
    print(f"Мой любимый цвет - {color}, а число - {number}")
    user_color = input("Введите свой любимый цвет:")
    user_number = int(input("Введите свое любимое число:"))
    print(f"Ваш любимый цвет - {user_color}, а число - {user_number}")


def second():
    seconds = input("Введите количество секунд:")
    if seconds.isdigit():
        seconds = int(seconds)
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60
        print(hours, minutes, seconds, sep=":")
    else:
        print("Введены неверные данные")


def third():
    number = input("Введите число:")
    if number.isdigit():
        number_2 = number * 2
        number_3 = number * 3
        result = int(number) + int(number_2) + int(number_3)
        print(f"{number} + {number_2} + {number_3} = {result}")
    else:
        print("Введены неверные данные")


def forth():
    number = input("Введите число:")
    biggest = 0
    if number.isdigit():
        number = int(number)
        while number > 0:
            tmp = number % 10
            if tmp > biggest:
                biggest = tmp
            number //= 10
        print("Самое большое число:", biggest)
    else:
        print("Введены неверные данные")


def fifth():
    earnings = int(input("Введите значение выручки:"))
    costs = int(input("Введите значение издержек:"))
    if earnings > costs:
        profit = earnings - costs
        print(f"Компания работает в прибыль, рентабельность выручки равна {profit / earnings:.2f}")
        workers = int(input("Введите количество работников:"))
        print(f"Прибыль фирмы на одного сотрудника: {profit/workers:.2f}")
    else:
        print("Компания работает в убыток")


def sixth():
    a = int(input("Введите результат первого дня в км:"))
    b = int(input("Введите желаемый результат в км:"))
    day = 1
    print(f"{day}-й день: {a:.2f} км")
    while a < b:
        day += 1
        a *= 1.1
        print(f"{day}-й день: {a:.2f} км")
    print(f"Вы достигните результата на {day} день")


# first()
# second()
# third()
# forth()
# fifth()
# sixth()
