from datetime import datetime

# variables

name = "Manoj"
age = 30
height = 5.8
is_student = True
# type conversion

age_str = "56"
print("Age as string", age_str, "is of type", type(age_str) )
age_int = int(age_str)
print("Age is a String: ", age_int, "is of type ", type(age_int))

newage = input("Enter your age: ");
if int(newage) > 18:
    print(f"{name} is an adult {datetime.now()}")
elif int(newage) == 18:
    print(f"{name} is just an adult")
else:
    print(f"{name} is not an adult")

