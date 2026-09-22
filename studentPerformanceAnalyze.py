# Name: Kaymer
# Period: PM
# Student Performance Analyzer

# This program will collect information about the student and use that information to calculate grades and make decisions about the student's academic performance.

print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print("")

# Login
print("Please login first")
username = input("Enter username: ")
pin = input("Enter PIN: ")

if username == "student":
    if pin == "1234":
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")

else:
    print("Login Failed: Incorrect username.")

print("")
print("Enter the student's information below.")
print("")

# name
name = input("What is the student's name? ")

# grade
grade = int(input("What grade level is the student in? "))

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
    return overall_grade
overall_grade = float(calculate_grade(assignment_ave, quiz_ave, test_ave))

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

# showing attendance status
def attendance_status(attendance):
    if attendance >= 95:
        print("Attendance Status: Excellent Attendance")
    elif attendance >= 90:
        print("Attendance Status: Good Attendance")
    elif attendance >= 80:
        print("Attendance Status: Attendance Warning")
    else:
        print("Attendance Status: Poor Attendance")

# Function for Missing Assignment Status
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Missing Assignment Status: Excellent")
    elif missing_assignments <= 2:
        print("Missing Assignment Status: Good")
    elif missing_assignments  <= 4:
        print("Missing Assignment Status: Warning")
    else:
        print("Missing Assignment Status: Critical")

# Nested Conditional: Academic Eligibility
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

# Nested Conditional: High Honors
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance>= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

# Check for good standing
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")

# Check for support
def check_support(overall_grade, attendance):
    if overall_grade <= 70 or attendance <= 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

# special grade level message
def grade_level_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("10 → Keep building your skills!")
    elif grade_level == 11:
        print("Junior year — keep pushing!")
    elif grade_level == 12:
        print("Senior year — finish strong!")
    else:
        print("Invalid grade level.")

# find out the strongest academic category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average == quiz_average == test_average:
        print("Strongest Category: Assignments, quiz, and test")
    elif assignment_average == quiz_average and assignment_average > test_average:
        print("Strongest Category: Assignments and quiz")
    elif quiz_average == test_average and test_average > assignment_average:
        print("Strongest Category: Test and quiz")
    elif assignment_average == test_average and assignment_average > quiz_average:
        print("Strongest Category: Assignments and test")
    elif assignment_average > quiz_average and assignment_average > test_average:
        print("Strongest Category: Assignments")
    elif quiz_average > assignment_average and quiz_average > test_average:
        print("Strongest Category: Quiz")
    else:
        print("Strongest Category: Test")

# Final summary
print("=============================================================")
print("                      STUDENT SUMMARY                        ")
print("=============================================================")
print("")
print("Student name: " + name)
print("Student grade level: " + str(grade))
print("")
print("Assignment Average: " + str(assignment_ave))
print("Quiz Average: " + str(quiz_ave))
print("Test Average: " + str(test_ave))
print("")
print("Attendance: " + str(attend_percent) + "%")
print("Missing Assignments: " + str(miss_assignment))
print("Overall Grade: " + str(overall_grade))
print("")
letter_grade(overall_grade)
print("")
attendance_status(attend_percent)
assignment_status(miss_assignment)
print("")
check_eligibility(overall_grade, attend_percent, miss_assignment)
print("")
check_high_honors(overall_grade, attend_percent, miss_assignment)
print("")
check_good_standing(overall_grade, attend_percent)
print("")
check_support(overall_grade, attend_percent)
print("")
strongest_category(assignment_ave, quiz_ave, test_ave)
print("")
grade_level_message(grade)
print("")
print("=============================================================")