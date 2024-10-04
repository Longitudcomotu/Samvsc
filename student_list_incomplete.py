# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
student=["Felix","Javier","Gilbert","Alex","Oaxac","Neftali","Peter","Andy","Pamela","Nick"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    #TODO HINT: Print each student in the 'students' list
    for i in student:
        print(i) 

# Add a new student to the list
def add_student():
    #TODO HINT: Ask the user for the student's name.
    newname=input("Enter new name ")
    #TODO Append the student's name to the 'students' list
    student.append(newname)
    
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# Remove a student from the list by name
def remove_student():
    #TODO HINT: Ask the user for the student's name to remove
    delname=input("What is the name you want to delete? ")
    #TODO Check if the student is in the list, then remove it
    if delname in student:
        student.remove(delname)
    #TODO If the student is not found, print an error message
    else:
        print("The name is not on the list ")
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# remove a student from the end of the list
def pop_student():
    #TODO HINT: Remove the last student from the list
    lastpop=student[-1]
    student.pop()
    
    #TODO If the list is not empty, display the name of the student removed
    print(f"you deleted {lastpop}")
    #TODO If the list is empty, print a message saying there are no students left
    if len(student) == 0:
        print("There are no students to delete")
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    upname=input("Enter the name of the student ")
    #TODO Check if the student is in the list, then ask for the new name
    if upname in student:
        index=student.index(upname)
        student[index]=input("Enter the update of the name ")

    #TODO Update the student's name in the list
    #TODO If the student is not found, print an error message
    else:
        print("Student not found")
    #TODO display the updated list
    display_students()
    #! After complete the function remove 'pass'

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        #TODO depending of the user choice option (1 - 5), call the correct function
        if choice=="5":
            break
        elif choice== "1":
            add_student()
        elif choice =="2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
# Start the program
menu()