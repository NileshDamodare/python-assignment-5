# Task 1: Dictionary of Student Marks

# Step 1: Create the dictionary
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

# Step 2: Ask user for input
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
