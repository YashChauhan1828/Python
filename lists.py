marks = [3,4,5,6,7]
print(marks)
print(marks[0])
for i in marks:
    print(i)

print(marks[-3])# negative index
print(marks[len(marks)-3])# positive index 
print(marks[5-3])# positive index  
print(marks[2])# positive index

if 5 in marks:
    print("Yes")
else:
    print("No")

if "as" in "yash":
    print("Yes")
else:
    print("No")

print(marks[:5:2])
print(marks[0:-2:2])

# List Comprehension

lst = [i*8 for i in range(10)]
print(lst)
lst = [i for i in range(10) if i%2==0]
print(lst)

