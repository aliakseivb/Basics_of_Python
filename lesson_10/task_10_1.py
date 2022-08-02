# 1. Реализовать класс Matrix (матрица).
# Формат вывода результата:
#
# Создать несколько матриц
# Вывести их с помощью print
# Выполнить сложение матриц и вывести результат сложения.
# Техническое задание:
#
# Данные в матрице хранятся как список списков целых чисел. Реализовать это через перегрузку конструктора.
# Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде - как в примере.
# Выравнивание чисел не обязательно, но желательно. Метод __str__() возвращает строку.
# Реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица. Метод __add__() возвращает новую матрицу.
# Исходные матрицы остаются неизменными.
# Сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.
# Подумайте о проверках корректности данных при создании матрицы и при их сложении
# Примеры/Тесты:
#
# >>> m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
# >>> m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
# >>> print(m1)
#
# |  11   2   3 |
# |   4   5   6 |
# | 117   8   9 |
#
# >>> print(m2)
#
# |   1   1   1 |
# |   1   1   1 |
# |   1   1   1 |
#
# >>> m3 = m1 + m2
# >>> print(m4)
#
# |  12   3   4 |
# |   5   6   7 |
# | 118   9  10 |
#
# >>> m4 = Matrix([[1,1],[1,1],[1,1]])
# >>> m5 = m1 + m4
# Traceback (most recent call last):
#   File "<interactive input>", line 1, in <module>
#   File "D:\\=WORK=\GEEKBRAINS\Python-I_files_\lesson-10\practical_task_solved\task_1.py",
#   line 40, in <span class="underline"><span class="underline">add</span></span>
#     raise ValueError("Incorrect dimensions for add method")
# ValueError: Incorrect dimensions for add method
# >>> m6 = Matrix([[1,1,1,1],[1,1,1],[1,1,1]])
# Traceback (most recent call last):
#   File "<interactive input>", line 1, in <module>
#   File "D:\\=WORK=\GEEKBRAINS\Python-I_files_\lesson-10\practical_task_solved\task_1.py",
#   line 11, in <span class="underline"><span class="underline">init</span></span>
#     raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")
# ValueError: Incorrect data for Matrix initialization: not equal lenght of lists
# >>>

# pеализовать класс Matrix (матрица).
class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix
        if len(self.__matrix) == 0:
            raise ValueError('Нулевая матрица. Уверены?')
        for i in range(len(self.__matrix) - 1):
            if len(self.__matrix[i]) != len(self.__matrix[i + 1]):
                if len(self.__matrix[i]) > len(self.__matrix[i + 1]):
                    error = str(self.__matrix[i])
                else:
                    error = str(self.__matrix[i + 1])
                raise ValueError(
                    f'Incorrect data for Matrix initialization: not equal lenght of lists - >>!! {error} !!<<')

    # Вывести их с помощью print
    def __str__(self):
        len_elem = [len(str(max(i))) for i in self.__matrix]
        max_el = max(len_elem)
        source = ''
        matrix_out = ''
        for k in range(len(self.__matrix[0])):
            source += '{: >' + f'{len_elem[k] + max_el}' + '} '  # не до конца правильно (матрица с длинными числами некрасивая), но хоть что-то  )))
        for i in self.__matrix:
            matrix_out += f'|{source.format(*i)}|''\n'
        return matrix_out

    # Выполнить сложение матриц и вывести результат сложения.
    def __add__(self, other):
        for i in self.__matrix:
            for k in other.__matrix:
                if len(i) != len(k):
                    raise ValueError("Incorrect dimensions for add method")
                else:
                    result = []
                    for item in zip(self.__matrix, other.__matrix):
                        result.append([sum([j, k]) for j, k in zip(*item)])
                    return Matrix(result)


if __name__ == '__main__':
    # Создать несколько матриц
    m1 = Matrix([[11, 2, 14], [4, 5, 31], [117, 8, 90]])
    m2 = Matrix([[1, 1, 1], [1, 11, 1], [1, 1, 1]])
    # m3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1, 1]])
    # m4 = Matrix([[1, 1], [1, 1], [1, 1]])
    m6 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(m1)
    print(m2)
    print(m6)
    m5 = m1 + m2 + m6
    print(m5)
