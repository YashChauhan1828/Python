data = {i:i**2 for i in range(6)} 
print(data)

data1 = {i:i**2 for i in range(6) if i%2==0} 
print(data)

ascii_char = {i:chr(i) for i in range(97,123)}
print(ascii_char)

fruits = ["apples","bananas","grapes","watermelon"]
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(fruit_dict)

alphabets = ["A","b","C","f"]
alphabets_ascii = {char:ord(char) for char in alphabets}
print(alphabets_ascii)

planingdrome = ["madam","racecar","amit","bob"]
palindrome_dict = {word:"yes" if word==word[::-1] else "no" for word in planingdrome}
print(palindrome_dict)

numbers=[121,222,34,56,789,111,90,434]
palindrome_num = {num:"yes" if str(num)==str(num[::-1]) else "no" for num in numbers}
print(palindrome_num)
