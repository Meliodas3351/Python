import random
from math import *
import numpy as np
from numpy import linalg

my_array = np.random.rand(10)
for i in range(len(my_array)):
    my_array[i] = random.randrange(10)
    floor(my_array[i])

print(my_array)
np.random.shuffle(my_array)
print(my_array)

# poor = int(input("Введите степень: "))
# for i in range(len(my_array)):
#     my_array[i] = my_array[i]**poor
#
# print(my_array)
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
my_array = linalg.matrix_power(matrix, 5)
#my_array = np.sort(my_array)
# for i in range(len(my_array)):
#     for j in range(i+1,len(my_array)):
#         if my_array[j]<my_array[i]:
#             x = my_array[j]
#             my_array[j] = my_array[i]
#             my_array[i] = x

print(my_array)