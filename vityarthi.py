# Student Marks Calculator

students = []

subjects = ["Maths", "CSE", "English", "EVS"]


def get_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def add_student():

    name = input("Enter student name: ")

    marks = []

    for subject in subjects:

        while True:

            try:
                mark = float(input("Enter marks for " + subject + ": "))

                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a number.")

    total = 0

    for mark in marks:
        total = total + mark

    percentage = total / 4

    grade = get_grade(percentage)

    result = "PASS"

    for mark in marks:

        if mark < 40:
            result = "FAIL"
            break

    student = [name, marks, total, percentage, grade, result]

    students.append(student)

    print("\nStudent added successfully.")


def show_students():

    if len(students) == 0:

        print("\nNo students added.")

    else:

        for student in students:

            print("\n----------------------------")
            print("Name:", student[0])

            print("Marks:")

            for i in range(4):
                print(subjects[i], ":", student[1][i])

            print("Total:", student[2], "/ 400")
            print("Percentage:", student[3], "%")
            print("Grade:", student[4])
            print("Result:", student[5])
            print("----------------------------")


def class_average():

    if len(students) == 0:

        print("\nNo student records available.")
        return

    total_percentage = 0

    for student in students:
        total_percentage = total_percentage + student[3]

    average = total_percentage / len(students)

    print("\n===== CLASS AVERAGE =====")
    print("Number of students:", len(students))
    print("Class average:", round(average, 2), "%")


def highest_marks():

    if len(students) == 0:

        print("\nNo student records available.")
        return

    highest = students[0]

    for student in students:

        if student[2] > highest[2]:
            highest = student

    print("\n===== HIGHEST MARKS =====")
    print("Student:", highest[0])
    print("Total marks:", highest[2], "/ 400")
    print("Percentage:", highest[3], "%")
    print("Grade:", highest[4])


def search_student():

    if len(students) == 0:

        print("\nNo student records available.")
        return

    search_name = input("\nEnter student name to search: ")

    found = False

    for student in students:

        if student[0].lower() == search_name.lower():

            print("\n===== STUDENT FOUND =====")
            print("Name:", student[0])

            print("Marks:")

            for i in range(4):
                print(subjects[i], ":", student[1][i])

            print("Total:", student[2], "/ 400")
            print("Percentage:", student[3], "%")
            print("Grade:", student[4])
            print("Result:", student[5])

            found = True

    if found == False:

        print("\nStudent not found.")


# Main Program

while True:

    print("\n================================")
    print("     STUDENT MARKS CALCULATOR")
    print("================================")

    print("1. Add Student")
    print("2. Show All Students")
    print("3. Class Average")
    print("4. Highest Marks")
    print("5. Search Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        show_students()

    elif choice == "3":

        class_average()

    elif choice == "4":

        highest_marks()

    elif choice == "5":

        search_student()

    elif choice == "6":

        print("\nProgram ended.")
        break

    else:

        print("\nInvalid choice. Please try again.")