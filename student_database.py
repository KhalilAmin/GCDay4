"""
create lists
print out welcome
ask for input
print out output
ask for additional info
validate input is correct
output info
ask for input to repeat

"""

student_name = ["Khalil", "John", "Carl", "Mark"]
hometown = ["Manhasset", "Miami", "Boston", "Charlotte"]
favorite_food = ["Pizza", "Burger", "Steak", "Fries"]

print("Welcome! Which student would you like to learn more about?")
validation = "y"
while validation == "y":
    for i in student_name:
        print(f'{int(student_name.index(i))+1}.{i}')
    student = int(input(f"Enter a number 1-{len(student_name)}: "))
    print(f'Student {student} is {student_name[student - 1]}. What would you like to know?')
    category = input('Enter "hometown" or "favorite food"> ').lower()

    while True:
        if category == "hometown":
            print(f"{student_name[student - 1]} is from {hometown[student -1]}. ")
            break
        elif category == "favorite food":
            print(f"{student_name[student - 1]}'s favorite food is {favorite_food[student -1]}. ")
            break
        else:
            category = input(f'That category does not exist. Please try again. Enter "hometown" or "favorite food" ')

    validation = input('Would you like to learn about another student? Enter "y" or "n": ').lower()

    # choose_category = True
    # while choose_category:
    #     if category == 'hometown' or category == 'favorite food':
    #         match category:
    #             case 'hometown':
    #                 print(f"{student_name[student - 1]} is from {hometown[student - 1]}. ")
    #                 choose_category = False
    #             case 'favorite food':
    #                 print(f"{student_name[student - 1]}'s favorite food is {favorite_food[student - 1]}. ")
    #                 choose_category = False
    #             case default:
    #                 break
    #     else:
    #         category = input(f'That category does not exist. Please try again. Enter "hometown" or "favorite food"')