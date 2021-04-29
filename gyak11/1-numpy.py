import numpy as np

elso_lista = [1, 2, 3]
array = np.array(elso_lista)
print("array", array)

matrix = np.array([[0, 2], [3, 4], [5, 6]])
print("dimenziók száma", matrix.ndim)  # 2
print("formája", matrix.shape)  # (3,2)
print("mérete", matrix.size)  # 6
print("adattípus", matrix.dtype)  # int32
print("elemméret (bájt)", matrix.itemsize)  # 4
print("típus", type(matrix))

matrix = [[1, 2, 3], [4, 5, 6]]

# indexelés pythonban
masodiksor_elso = matrix[1][0]  # 4
print("masodiksor_elso", masodiksor_elso)

# numpy indexelés
matrix = np.array(matrix)  # hogy lista helyett ndarray legyen
masodiksor_elso = matrix[1, 0]  # 4
print("masodiksor_elso", masodiksor_elso)

matrix = np.array([[0, 2], [3, 4], [5, 6]], ndmin=8)
print(matrix)
matrix = np.array([[0, 2], [3, 4], [5, 6]], dtype=float)
print(matrix)
matrix = np.array([[0, 2], [3, 4], [5, 6]], dtype=np.float64)
print(matrix)
matrix.dtype = complex
print(matrix)
matrix = np.array([[0, 2], [3, 4], [5, 6], [7, 8]])
# matrix.shape = (8, 2)
matrix.shape = (4, 2)
print("4*2", matrix)
matrix.shape = (8, 1)
print("8*1", matrix)
b = matrix.reshape(2, 4)
print("2*4", b)
print(b.flags)

# index tömbbel
array = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2])
index = np.array([3, 4, 2, 3])  #
x = array[index]  # [7,6,8,7]
print("x", x)

# üres mátrix
arr0 = np.empty((3, 3))
print(arr0)

# teli 0 mátrix
arr1 = np.zeros((2, 3))  # paramétere egy int vagy tuple, ami a méretét adja meg
print("arr1", arr1)
# [[0,0,0],
# [0,0,0]]

# teli 1 mátrix
arr2 = np.ones((1, 2))  # paramétere egy int vagy tuple, ami a méretét adja meg
# [[1,1]]
print("arr2", arr2)
# teli n mátrix
arr3 = np.full((2, 3), 5)  # paraméterei egy int vagy tuple, ami a méretét adja meg és egy valós szám, ami a tömb elemeit
print("arr3", arr3)

# python range-hez hasonlóan
arr3 = np.arange(10)  # [0,1,2,3,4,5,6,7,8,9]
arr4 = np.arange(2, 5, 2)  # [2,4]
arr5 = np.arange(1, 20, 0.7)  # [2,4]
print(arr5)
# paraméterei az intervallum eleje (opcionális), vége és a lépésköz

# adott invervallumon n db szám létrehozása egyenletes közzel
arr6 = np.linspace(0, 4, 6)  # [0,0.8,1.6,2.4,3.2,4]
# paraméterei az intervallum eleje, vége és hogy hány számot szeretnénk
print(arr6)

x = [1, 2, 3]
y = [4, 5, 6]
z = []
for i in range(len(x)):
    z.append(x[i] + y[i])

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = x + y
print("x+y", z)
print("x*y", x * y)
print("x*3", x * 3)
print("x*y", x @ y)

x = np.random.rand(3, 5)
print(x)
osszeg = np.sum(x)  # lista vagy mátrix elemeinek összege
print("osszeg", osszeg)
print("sum", np.sum(x))
print("sin", np.sin(x))
print("prod", np.prod(x))
print("mean", np.mean(x))
print("std", np.std(x))
print("var", np.var(x))
print("min", np.min(x))
print("max", np.max(x))
print("argmin", np.argmin(x))
print("argmax", np.argmax(x))

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

matrixszorzat = np.dot(matrix1, matrix2)  # mátrixszorzás (nem elemenként)
print("matrixszorzat", matrixszorzat)
print("matrixszorzat", matrix1 @ matrix2)

arr = np.arange(12)  # [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
matrix = arr.reshape(4, 3)  # [[ 0,  1,  2],
# [ 3,  4,  5],
# [ 6,  7,  8],
# [ 9, 10, 11]]
# vissza vektorrá
arr2 = matrix.reshape(-1)  # [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
print("arr2", arr2)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr3 = np.hstack((arr1, arr2))  # [[1, 2, 5, 6],
# [3, 4, 7, 8]]

arr4 = np.vstack((arr1, arr2))  # [[1, 2],
# [3, 4],
# [5, 6],
# [7, 8]]

array = np.array([np.arange(0, 10, 1), np.arange(10, 0, -1), np.arange(20, 10, -1)])
print(array)
print("- array[::2]\n", array[::2])
print("- array[:, ::-1]\n", array[:, ::-1])
print("- array[::, ::2]\n", array[::, ::2])

array = np.array([1, 2, 3, 4, 5])
print(array > 3)
print(array != 3)
print(array[array > 3])
print(np.where(array > 3, 20, 1))

array = np.random.rand(20)
array = np.sort(array)
print(array)
