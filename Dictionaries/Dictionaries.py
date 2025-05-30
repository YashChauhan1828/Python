#  After python 3.7 dictionaries are ordered while sets are unordered

dict = {
    "Name" : "Yash",
    "Enrollment_No" : "ET22BTIT013"
}
print(dict)
print(dict["Name"])# Throws error if key does not exist
print(dict.get("Enrollment_No")) # Returns None if key does not exist
print(dict.keys())
for key in dict.keys():
    print(dict[key])
print(dict.values())
print(dict.items())
for key, value in dict.items():
    print(f"{key} : {value}")