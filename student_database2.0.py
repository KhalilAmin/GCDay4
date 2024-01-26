student_list = [{ "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
               { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
               { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }]

def list_names(students):
    for student in students:
        if "name" in student:
            print(f'{students.index(student)+1}. {student["name"]}')

def get_new_student():
    new_name = input('Please input a name for the new student:\n> ')
    new_hometown = input('Please input their hometown:\n> ')
    new_food = input('Please input their favorite food:\n> ')
    new_student = {"name": new_name, "hometown": new_hometown, "favorite_food": new_food}
    return new_student

action = input("Please select which action you'd like to do: add, view, or quit\n> ")
while True:
    if action == "add":
        student_list.append(get_new_student())
        break
    elif action == "view":
        list_names(student_list)
        student_index = int(input(f"Which student would you like to learn more about? Enter a number 1-{len(student_list)}:\n> "))
        student_choice = student_list[student_index-1]
        student_info = input(f'Student {student_index} is {student_choice["name"]}. What would you like to know?\n\tEnter "hometown" or "favorite food"\n> ')
        if student_info == "hometown":
            print(f'{student_choice["name"]} is from {student_choice["hometown"]}.')
        elif student_info == "favorite food":
            print(f'{student_choice["name"]} loves {student_choice["favorite_food"]}.')
        break
    elif action == "quit":
        print("Good bye!")
        break
    else:
        action = input(f'This action does not exist. Please try again. Enter "add", "view" or "quit" ')

list_names(student_list)