import random

n = int(input("Please enter count of columns - "))
m = int(input("Please enter count of rows - "))

A = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        A[j][i] = random.randint(0, 50)
        print(A[j][i], end=" ")
    print()

sum = 0

for j in range(n):
    sum += A[j][0]
    sum += A[j][m-1]
print(sum)


