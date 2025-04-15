students = {}

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    subject = input("Enter subject: ")
    marks = input("Enter marks: ")
    
    students[name] = {
        "age": age,
        "subject": subject,
        "marks": marks
    }
    print(f"{name} added successfully!\n")

    
def view_student():
    if students:
        for name, info in students.items():
            print(f"Name: {name}, Age: {info['age']}, Subject: {info['subject']}, Marks: {info['marks']}")
    else:
        print("Not found")
        
def search_student():
    name = input("Enter name to be searched: ")
    if name in students:
        info = students[name]
        print(f"Age: {info['age']}, Subject: {info['subject']}, Marks: {info['marks']}")
        
    else:
        print("Not found")
                
while True:
    print("\n1. Add student\n2. View students\n3. Search student\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Bye! 👋")
        break
    else:
        print("Invalid option.\n")