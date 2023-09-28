import numpy as np

matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
def transpone():
    b = matrix1.T
    print(b)

matrix2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

def umn():
    umn = np.dot(matrix1, matrix2)
    print(umn)

def rang():
    rang = np.linalg.matrix_rank(matrix1)
    print(rang)
print('введите число для программы:')
print('1- транспонирование матрицы ')
print('2- умножение матрицы')
print('3- вычесление ранга матрицы')
a = int(input())
if a == 1:
    transpone()
elif a == 2:
    umn()
elif a == 2:
    rang()
else:
    print('такой программы нет')







