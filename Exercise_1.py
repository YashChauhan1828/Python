import time
timestamp =time.strftime("%H:%M:%S")
print("Current time is : ",timestamp)
hour = int(time.strftime("%H"))
minute =int(time.strftime("%M"))
second =int(time.strftime("%S"))
timer = hour,minute,second

if(timer > (0,0,0) and timer < (11,59,59)):
    print("Good Morning Sir")
elif(timer > (12,0,0) and timer < (16,59,59)):
    print("Good Afternoon Sir")
elif(timer < (17,0,0) and timer < (20,59,59)):
    print("Good Evening Sir")
else:
    print("Good Night Sir")

