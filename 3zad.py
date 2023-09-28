import timeit
def test(n):
    return sum(range(n))
n = 10000
loop = 1000
result = timeit.timeit('test(n)', globals=globals(), number=loop)
print(result / loop)

matrix =[[5,4],[4,5]]
def inverse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        raise print("Матрица должна быть квадратной")
    extended = []
    for i in range(rows):
        row = matrix[i] + [int(i == j) for j in range(cols)]
        extended.append(row)
    for i in range(rows):
        p = extended[i][i]
        if p == 0:
            raise print("Матрица необратима")
        for j in range(cols * 2):
            extended[i][j] /= p
        for k in range(rows):
            if k != i:
                factor = extended[k][i]
                for j in range(cols * 2):
                    extended[k][j] -= factor * extended[i][j]
    inverse = []
    for i in range(rows):
        inverse.append(extended[i][cols:])

    return inverse
u = inverse(matrix)
print(u)


