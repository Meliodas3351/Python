import numpy as np

my_array = np.arange(1, 100, 3)
print(my_array)
print(my_array.size)

my_list = my_array.tolist()
print(my_list)
print(len(my_list))

second_array = np.array(my_list)
print(second_array)

count = 0
my_list = []
for i in my_array:
    if i not in my_list:
        my_list.append(i)
        count += 1

print(str(count) + " different numbers")

count = 0
mini_count = 0

for i in my_array:
    if i <= 0:
        if mini_count > count:
            count = mini_count
        mini_count = 0
    else:
        mini_count += 1

if mini_count > count:
    count = mini_count
    mini_count = 0

print(str(count) + " numbers > 0 inline")
list1 = [1,2,3,4,5]
new_array = np.hstack((my_array, list1))
print(new_array)

my_array = np.arange(100).reshape(10, 10)
print(my_array)
print(np.array_split(new_array, 2))

my_array = np.arange(1, 100, 3)
array1 = my_array[0: 5]

array2 = my_array[5:]

print(array1)
print(array2)

x = my_array.copy()
print(x)
