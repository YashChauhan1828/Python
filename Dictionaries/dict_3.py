college_students = {
    "1001": {
        "name": "Anjali Mehta",
        "department": "Computer Engineering",
        "year": "2nd Year",
        "courses": {
            "DSA": 88,
            "OOP": 91,
            "Maths": 79
        }
    },
    "1002": {
        "name": "Ravi Patel",
        "department": "Electronics",
        "year": "3rd Year",
        "courses": {
            "Microprocessors": 85,
            "Signals": 74,
            "Maths": 80
        }
    },
    "1003": {
        "name": "Sneha Sharma",
        "department": "Mechanical",
        "year": "1st Year",
        "courses": {
            "Physics": 90,
            "Workshop": 95,
            "Maths": 87
        }
    }
}


print(college_students["1001"]["name"])  


print(college_students["1002"]["courses"]["Signals"])  

college_students["1003"]["courses"]["Engineering Drawing"] = 89


college_students["1001"]["year"] = "3rd Year"

for student_id, details in college_students.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {details['name']}")
    print(f"Department: {details['department']}")
    print(f"Year: {details['year']}")
    print("Courses and Marks:")
    for course, mark in details["courses"].items():
        print(f"  {course}: {mark}")
    print("-" * 40)