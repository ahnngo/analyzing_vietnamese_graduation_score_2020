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

print(combination_percentage)

# selecting outstanding data for visualization
combination_for_chart = []
other = 0
for i in range(len(number_of_exams_taken)):
    if number_of_exams_taken[i] > 2000:
        combination_for_chart.append(number_of_exams_taken[i])
    else:
        other += number_of_exams_taken[i]
combination_for_chart.append(other)

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
y = np.array(combination_for_chart)
mylabels = [None, None, None, "86.32%", None]
myexplode = [0, 0, 0, 0.2, 0]

plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode)
plt.legend(title = "Number of exams by students:", loc='upper right', labels=["3 subjects", "4 subjects", "6 subjects", "7 subjects", "others"])
plt.show() 