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

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

# loop through students to find students who did not take the exam
for student in students:
    # iterate through all subjects
    for i in range(5,16):
        if student[i] == "-1":
            not_take_exam[i-5] += 1


not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

# calculate percentage of each not_take_exam component
for i in range(0,11):
    not_take_exam_percentage[i] = round((not_take_exam[i] / total_student * 100),2)

# plot bar chart
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

# numpy list from 0-11
y_pos = np.arange(len(subjects))

subjects = ["math", "literature", "socialsc", "naturalsc", "history", "geography", "civics", "biology", "physics", "chemistry", "english"]

# plot the barchart using 2 list
plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)

# change horizontal category name 
plt.xticks(y_pos, subjects)

# set limit to y axis
axis.set_ylim(0,100)

# lbale and title 
plt.ylabel('Percentage')
plt.title('The numbers of student did not take or did not sign up for an exam')

# make label on top of each bar
rects = axis.patches

for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 2, label, ha="center", va="bottom")

plt.show()