
number_people = int(input("Enter the number of people attending the trip: "))
minimum_height = 1.5
minimum_age = 16
people_list = []
for x in range(number_people):
    name = input("Name of person: ")
    height = float(input("Height of person: "))
    age = int(input("Age of person: "))
    if height < minimum_height and age < minimum_age:
        print("Person is not old enough and not tall enough.")
    elif height < minimum_height:
        print("Person is not tall enough.")
    elif age < minimum_age:
        print("Person is not old enough.")
    else:
        print("Person is old enough and tall enough.")
        people_list.append(name)

print(people_list)
