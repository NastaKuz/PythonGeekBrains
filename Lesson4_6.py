"""6. Реализовать два небольших скрипта: а) итератор, генерирующий целые числа, начиная с указанного, б) итератор,
повторяющий элементы некоторого списка, определенного заранее. Подсказка: использовать функцию count() и cycle()
модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
условие его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
прекращено. """
from itertools import count
from itertools import cycle


def count_iter(start_number, finish_number):
    for el in count(start_number):
        if el > finish_number:
            break
        else:
            print(el)


def cycle_iter(my_list, iteration):
    i = 0
    iterator = cycle(my_list)
    while i < iteration:
        print(next(iterator))
        i += 1


count_iter(int(input("С какого числа начинаем отсчет: ")), int(input("На каком числе останавливаемся: ")))
cycle_iter([1, 2, 3, 4, 5], int(input("Сколько итераций делаем: ")))


