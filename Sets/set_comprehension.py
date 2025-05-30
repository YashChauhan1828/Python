# data2 = {i for i in range(1, 10)}
# print(data2)

# data =["bob","ram","racecar","parth","naman"]
# data1 = set(data)
# palingdrome = { i for i in data1 if i == i[::-1]}
# print(palingdrome)

# cities = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda","baroda","rajkot"]
# set1 = set(cities)
# city = {i[0].lower() for i in set1}
# print(city)

events = [{"Ahme_Event":["ram","amit","shyam","ram"]},{"Udaipur_Event":["ram","amit","kunal"]},{"mumbai_Event":["ram","parth","amit","ajay","jay"]}]
set1 = set({})
set2 = set({})
set3 = set({})
event1=events[0]
event2=events[1]
event3=events[2]
for event,participants in event1.items():
    print(event)
    for participant in participants:
        set1.add(participant)
    print()

for event,participants in event2.items():
    print(event)
    for participant in participants:
        set2.add(participant)
    print()

for event,participants in event3.items():
    print(event)
    for participant in participants:
        set3.add(participant)
    print()
print(set1)
print(set2)
print(set3)
print((set1.intersection(set2)).intersection(set3))