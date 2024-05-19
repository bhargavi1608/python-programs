# Kapil just received his examination marks for all subjects. In his hurry, he forgot to check
# his grade for each subject. He is also too worried to calculate his grades.
# Write a program to take the marks in each subject and print out the grade for that
# subject.
# ● If the marks are less than 35, the grade is F.
# ● If the marks are 35 or above and less than 60, the grade is C.
# ● If the marks are above 60 and below 80, the grade is B.
# ● If the marks are 80 or above, the grade is A.
# Marks can have up to 2 decimal places. Marks should be rounded to the nearest whole
# number before a grade is declared.
# Your program should accept marks in each subject on a separate line and print the
# grade for each line.
# Example:34.72
# 35
# 34
# 45.63
# 80.23
# 79.46

# Output: C
# C
# F
# C
# A
# B
# Function to calculate grade based on marks
def calculate_grade(marks):
    rounded_marks = round(marks)  # Round marks to the nearest whole number
    if rounded_marks < 35:
        return "F"
    elif 35 <= rounded_marks < 60:
        return "C"
    elif 60 <= rounded_marks < 80:
        return "B"
    else:
        return "A"

# Input marks for each subject
num_subjects = int(input("Enter the number of subjects: "))
print("Enter marks for each subject:")

# Iterate over each subject
for i in range(num_subjects):
    marks = float(input())
    grade = calculate_grade(marks)
    print(grade)