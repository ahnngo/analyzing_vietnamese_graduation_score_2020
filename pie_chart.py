with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

# remove last student (empty student)
students.pop()

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student in list
for i in range(len(students)):
    students[i] = students[i].split(",")

number_of_exams_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

# loop through students to find students took each exam
for student in students:
    # iterate through all subjects
    total_exam_taken = 0
    for i in range(5,16):
        if student[i] != "-1":
            total_exam_taken += 1

    number_of_exams_taken[total_exam_taken] += 1

combination_percentage = [0,0,0,0,0,0,0,0,0,0,0,0]

total_combination = 0
for i in range(len(number_of_exams_taken)):
    total_combination += number_of_exams_taken[i]

for i in range(len(combination_percentage)):
    combination_percentage[i] = round((number_of_exams_taken[i]/total_combination*100),2)


import matplotlib.pyplot as plt
print(combination_percentage)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
sizes = [0.0, 0.11, 0.16, 3.49, 5.82, 0.43, 3.67, 86.32, 0.0, 0.0, 0.0, 0.0]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

print(len(students) == total_combination)

plt.show()