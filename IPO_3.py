print("Enter number:")
num = int(input())
k = 0
while num > 0:
    k = k * 10 + num % 10
    num //= 10
print(k)
