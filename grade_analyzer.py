students = [
    "Ethan Walker",
    "Olivia Martinez", 
    "Liam Thompson", 
    "Ava Robinson", 
    "Noah Hernandez", 
    "Isabella Clark", 
    "Mason Lewis", 
    "Sophia Hall", 
    "Lucas Allen",
    "Mia Young",
    "Jacob King",
    "Emily Wright", 
    "Daniel Scott"
    ]

grades = [98, 96, 87, 84, 82, 79, 77, 74, 65, 63, 51, 36, 34]
passing_grades = []
curved_grades = []

print("----- TEST RESULTS -----\n")
for i in range(len(grades)):
    print(students[i] + ": " + str(grades[i]))

print("\n")

for grade in grades:
    if grade > 75:
        passing_grades.append(grade)

for grade in grades:
    curved_grades.append(grade + 2)

passing_after_curve = [grade for grade in curved_grades if grade >= 75]

students_before_curve = []
for i in range(len(grades)):
    if grades[i] >=75:
        students_before_curve.append(students[i])

students_after_curve = []
for i in range(len(curved_grades)):
    if curved_grades[i] >= 75:
        students_after_curve.append(students[i])

print("----- Students who passed BEFORE the curve: -----\n")
print(students_before_curve)
print("\n")
print("----- Students who passed AFTER the curve: -----\n")
print(students_after_curve)

print("\n")
print("----- Big Congradulations to these students! You passed! -----\n")
for student in students_after_curve:
    print(student)

    
