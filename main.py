class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


students = []

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Exit")
    print("4.Delete Student")
    print("5.Save students")
    print("6.Load students")
    print("7.update age")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        students.append(Student(name,age))
        print("Student added successfully")

    elif choice == "2":
        if not students:
            print("No students available")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        print("Program stopped")
        break

    elif choice == "4":
        name = input("Enter student name to delete: ")
        found = False

        for student in students:
            if student.name == name:
                students.remove(student)
                print("Student removed")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "5":
      with open("students.txt","w") as file:
        for student in students:
            file.write(f"{student.name},{student.age}\n")
        print("Students saved successfully")

    elif choice == "6":
    
        with open("students.txt","r") as file:
            students.clear()
            for line in file:
                name, age = line.strip().split(",")
                students.append(Student(name, int(age)))

        print("Students loaded successfully")

    
        
    elif choice == "7":
    name = input("Enter student name to update age: ")
    found = False

    for student in students:
        if student.name == name:
            new_age = int(input("Enter new age: "))
            student.age = new_age
            print("Age updated successfully")
            found = True
            break

    if not found:
        print("Student not found")

    else:
        print("Invalid choice")