import random


x = 4
y = 4
#array = [[random.randint(0, 1) for i in range(x)] for j in range(y)]
array = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

is_reflective = all([array[i][j] == 1 for i, elem in enumerate(array) for j, val in enumerate(elem) if i == j])
print(is_reflective)

is_not_reflective = all([array[i][j] == 0 for i, elem in enumerate(array) for j, val in enumerate(elem) if i == j])

is_symmetrical = all([array[i][j] == 1 and array[j][i] == 1 for i, elem in enumerate(array) for j, val in enumerate(elem)])

is_antisymmetric = all([array[i][j] == 1 and array[j][i] == 0 for i, elem in enumerate(array) for j, val in enumerate(elem)])