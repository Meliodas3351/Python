import random


def findSum(matrix, size, step):
    sum1 = 0
    sum2 = 0
    for i in range(size):
        sum1 += matrix[i][i]
        sum2 += matrix[i][size - i - 1]
    if step == 1:
        return sum1
    else:
        return sum2


n = int(input("Please enter size of matrix - "))

A = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        A[j][i] = random.randint(0, 50)
        print(A[j][i], end=" ")
    print()
print("Enter 1 if you want to sum the elements of the main diagonal, and -1 - if the side diagonal")
k = int(input())
mySum = findSum(A, n, k)
print(mySum)
