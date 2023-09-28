import timeit
import numpy as np
def test(n):
    return sum(range(n))

n = 10000
loop = 1000

result = timeit.timeit('test(n)', globals=globals(), number=loop)
print(result / loop)


a = np.array([[1, 3], [2, 1]])
result = np.linalg.matrix_power(a,-1)
print(result)
