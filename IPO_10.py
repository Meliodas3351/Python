arr = []
myStr = str(input())
arr.append(myStr)
while myStr != "":
    myStr = str(input())
    arr.append(myStr)
f = open('text.jpg', 'w')
for index in arr:
    f.write(index + '\n')
f1 = open('text.jpg', 'r')
print(f1.read())
f.close()