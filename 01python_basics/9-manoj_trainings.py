
course_catalog = {
    "BTP_BASICS": {"trainer": "Suresh", "Fees": 15000, "hours": 20},
    "ABAP_CLOUD": {"trainer": "Priya", "Fees": 28000, "hours": 45},
    "HANA_DB": {"trainer": "Vikas", "Fees": 22000, "hours": 35},
    "FIORI_ELEMENTS": {"trainer": "Anjali", "Fees": 18000, "hours": 30},
    "SAP_BUILD": {"trainer": "Rohan", "Fees": 10000, "hours": 15},
    "CPI_INTEGRATION": {"trainer": "Meera", "Fees": 26000, "hours": 40},
    "SUCCESSFACTORS": {"trainer": "Amit", "Fees": 30000, "hours": 50},
    "DATA_SPHERE": {"trainer": "Lekha", "Fees": 24000, "hours": 25},
    "RAP_MODEL": {"trainer": "Karthik", "Fees": 27000, "hours": 40},
    "SAC_ANALYTICS": {"trainer": "Deepa", "Fees": 21000, "hours": 32}
}


selected_courses = []

while True:
    course = input("Enter the course name").strip().upper()
    if course == 'EXIT':
        break
    elif course in course_catalog:
        selected_courses.append(course)
        print(f"Added {course} to your selection")
    else:
        print(f"Course {course} not found")

print("/n selected courses:")
total_amount = 0

for idx, course in enumerate(selected_courses, start=1):
    details = course_catalog[course]
    total_amount += details['Fees']

print(f"Total Price : {total_amount}")

