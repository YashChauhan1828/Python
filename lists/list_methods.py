l=[1,2,3,4,5,2,7,4,2,1,1,1]

l.append(9)
l.sort(reverse=True)
l.reverse
print(l.index(2))
print(l.count(2))
# m=l
# m[0]=0
# print(l)
m=l.copy()
m[0]=0
print(l)
l.insert(1,999)
n=[900,200,1000]
# l.extend(n)
h=l+n
print(h)
# print(l)
