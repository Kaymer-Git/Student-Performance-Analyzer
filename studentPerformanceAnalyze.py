# Name: Kaymer
# Period: PM
# Student Performance Analyzer

# This program will collect information about the student and use that information to calculate grades and make decisions about the student's academic performance.

print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print("Enter the student's information below.")

# name
name = input("What is the student's name? ")

# grade
grade = input("What grade level is the student in? ")

# assignment average
assignment_ave = float(input("What is the student's assignment average?"))

# quiz average
quiz_ave = float(input("What is the student's quiz average?"))

#test average
test_ave = float(input("What is the student's test average?"))

# attendance
attend_percent = float(input("What is the student's attendance percentage?"))

# missing assignments
miss_assignment = int(input("How many missing assignments does the student have?"))

# create a function to calculate the overall grade
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 3/10
    quiz_portion = quiz_average * 3/10
    test_portion = test_average * 4/10
    overall_grade = assignment_portion + quiz_portion + test_portion
    print("Overall grade: " + str(overall_grade))

# create a function to make letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        print("Letter grade: A")
    elif overall_grade >= 80:
        print("Letter grade: B")
    elif overall_grade >= 70:
        print("Letter grade: C")
    elif overall_grade >= 60:
        print("Letter grade: D")
    else:
        print("Letter grade: F")