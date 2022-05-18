s = ""
n = int(input())
for i in range(n):
    myStr = str(input())
    s += myStr + " "
arr = s.split()
print(arr)
d = dict()
for i in arr:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] = d.get(i) + 1
maxInt = 0
myStr = ""
for i in d:
    if d.get(i) > maxInt:
        maxInt = d.get(i)
        myStr = i
    elif d.get(i) == maxInt and len(i) < len(myStr):
        maxInt = d.get(i)
        myStr = i
d.update()
print(d)
d.popitem()
print(d)
print(myStr)
