s1={3,4,5,6,7,8}
s2={1,2,9,8,5,0}
print(s1 , s2)
# s1.update(s2)
print(s1.union(s2))
print(s1)
# s1.intersection_update(s2)
# print(s1)
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
cities = {"surat" , "Banglore" , "Ahmedabad" , "Chennai"}
cities2 = {"surat" , "Ahmedabad"}
print(cities.issuperset(cities2))
print(cities2.issubset(cities))
cities3 = {"Dubai" , "Sydney"}
cities.add("California")
cities.update(cities3)
print(cities)
cities.remove("California")
print(cities)
item = cities.pop()
print(item)
cities.discard("Dubai")
print(cities)
cities.discard("surat")
print(cities)
# del cities // delete the set
# cities.clear()
# print(cities)
if "surat" in cities:
    print("surat is in cities")
else:
    print("surat is not in cities")