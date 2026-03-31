from student import Student
from file_manager import save_students, load_students

filename = "students.json"
students = load_students(filename)

while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    enter_input = input("Enter input for choice..")


    if enter_input == "1":
        name = input("enter  student  name")
        try:
            marks = int(input("enter the marks"))
            s= Student(name, marks)
            students.append(s.to_dict())
            save_students(filename, students)
        except ValueError as e:
            print("Marks must be a number")
            continue
    elif enter_input == "2":
        for s in students:
            print(s["name"],s["marks"],s["grade"])
    elif enter_input == "3":
        break

