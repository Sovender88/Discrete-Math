import random

array = [[random.randint(0, 1) for i in range(4)] for j in range(4)]
rel = {(i, j) for i, elem in enumerate(array) for j, val in enumerate(elem) if array[i][j] == 1}
print(rel)

def is_transitive(rel):
    seconds_elements = {b for (a, b) in rel}
    for (a, b) in rel:
        for c in seconds_elements:
            if (b, c) in rel and (a, c) not in rel:
                return False
    return True
print(is_transitive(rel))