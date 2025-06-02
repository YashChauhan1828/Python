numbers = [1,2,3,4,5,6,7,8,9]

def even_numbers(data):
    for i in data:
        if i%2==0:
            yield i 
data = even_numbers(numbers)
for i in data:
    print(i)
