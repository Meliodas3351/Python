n = int(input("Please enter size of array - "))
arr = []

for i in range(n):
    arr.append(int(input()))
min = arr[1]
minIndex = 0

for i in range(n):
    if abs(arr[i]) < min:
        min = arr[i]
        minIndex = i
print("Index of min element - ", minIndex)
