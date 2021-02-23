""". Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для
реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д. """


class Matrix:
    def __init__(self, list_of_lists):
        self.cols = len(list_of_lists[0])
        self.rows = len(list_of_lists)
        self.matrix = list_of_lists

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, list_of_lists):
        result = []  # подгоняем все списки под размерность первого, чтобы получить прямоугольник
        for i in list_of_lists:
            if len(i) < self.cols:
                result.append(i + [0] * (self.cols - len(i)))
            elif len(i) > self.cols:
                result.append(i[:self.cols])
            else:
                result.append(i)
        self.__matrix = result

    def __add__(self, matrix_2):
        if self.rows == matrix_2.rows and self.cols == matrix_2.cols:
            result = [[sum(j) for j in zip(*i)] for i in zip(self.matrix, matrix_2.matrix)]
            return Matrix(result)
        else:
            return "Размерность матриц не совпадает"

    def __str__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.matrix])


mat = Matrix([[1, 2, 3], [4, 5, 6]])
print(f"Первая матрица: \n{mat}")
mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(f"Вторая матрица: \n{mat2}")
print(f"Сумма матриц: \n{mat + mat2}")
