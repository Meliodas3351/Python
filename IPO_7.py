a = set('fdsjfghk')
b = set('ffjefhrhj')
c = set('poiutnghfrew')
kortegh = (a, b, c,)
print(kortegh)
myStr = str(a)
mySet = set(kortegh[1])
for i in range(1, len(kortegh), 1):
    mySet = kortegh[i] & mySet
mySet -= kortegh[0]
print(mySet)
