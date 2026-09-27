# Student Marks Calculator

## Project Description

Student Marks Calculator is a beginner-level Python command-line project.

The program allows the user to enter and manage marks for four subjects:

* Maths
* CSE
* English
* EVS

It calculates the total marks, percentage, grade, and pass/fail result.

The program also includes class average calculation, highest marks calculation, and student search.

## Features

* Add student details
* Enter marks for four subjects
* Calculate total marks
* Calculate percentage
* Calculate grade
* Check pass/fail result
* Display all students
* Calculate class average
* Find highest marks
* Search for a student by name
* Validate marks between 0 and 100

## Requirements

* Python 3.x
* Terminal or Command Prompt

No external Python libraries are required.

## Project Structure

```text
StudentMarksCalculator/
│
├── main.py
└── README.md
```

## How to Run

### 1. Download the Project

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Open the project folder:

```bash
cd StudentMarksCalculator
```

### 2. Run the Program

Run the following command:

```bash
python main.py
```

If `python` does not work, try:

```bash
python3 main.py
```

## How the Program Works

When the program starts, it displays a menu:

```text
================================
     STUDENT MARKS CALCULATOR
================================

1. Add Student
2. Show All Students
3. Class Average
4. Highest Marks
5. Search Student
6. Exit
```

### Add Student

Choose option `1` and enter:

* Student name
* Maths marks
* CSE marks
* English marks
* EVS marks

The program calculates the total, percentage, grade, and result.

### Show All Students

Choose option `2` to display all students entered during the current program session.

### Class Average

Choose option `3` to calculate the average percentage of all students.

### Highest Marks

Choose option `4` to find the student with the highest total marks.

### Search Student

Choose option `5` and enter a student's name to search for their result.

### Exit

Choose option `6` to close the program.

## Grading System

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| 40–49      | E     |
| Below 40   | F     |

A student must score at least 40 marks in every subject to pass.

## Example

```text
Enter your choice: 1

Enter student name: Raunak
Enter marks for Maths: 90
Enter marks for CSE: 92
Enter marks for English: 85
Enter marks for EVS: 88

Student added successfully.
```

The result will be:

```text
Name: Raunak
Total: 355 / 400
Percentage: 88.75 %
Grade: A
Result: PASS
```

## Python Concepts Used

The project uses:

* Variables
* Lists
* Functions
* User input
* `if-elif-else`
* `for` loops
* `while` loops
* `break`
* Arithmetic operations
* String operations
* Searching
* Summation
* Average calculation
* Maximum value calculation
* Exception handling

## Limitations

* Student records are stored only while the program is running.
* The program currently uses four fixed subjects.
* It is a command-line application.
* No external database is used.

## Future Improvements

Possible improvements include:

* Saving student records to a file
* Editing student marks
* Deleting student records
* Adding student roll numbers
* Adding more subjects
* Exporting results to CSV
* Creating a graphical user interface

## Author

**Raunak Mehta**

Python Essentials - Evaluated Course Project
