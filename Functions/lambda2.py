even_or_odd = lambda x : "Even" if x%2==0 else "Odd"
print(even_or_odd(15))

maximum = lambda x,y : "max" if x>y else "min"
print(maximum(10,20))

pass_or_fail = lambda score : "Pass" if score>=35 else "Fail"
print(pass_or_fail(40))

check_number = lambda x : "positive" if x>0 else ("zero" if x==0 else "negative")
print(check_number(-5))

grade = lambda perc : "A" if perc>=80 else ("B" if perc>=70 else "C")
print(grade(90))