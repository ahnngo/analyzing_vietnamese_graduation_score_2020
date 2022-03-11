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

# get number pf student per age group
# 2003 2002 2001 ...
# 17 18 19 ... 
number_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
avg_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]

# find num of students in each age group
for student in students:
    age =  2020 - int(student[4])
    if age >= 27:
        age = 27
    number_of_student_per_age_group[age - 17] += 1

    # find the total score of each age group
    sum_score = 0 # sum of score
    count_score = 0 # number of taken exams
    for i in range(11):
        if student[i+5] != "-1":
            count_score += 1
            sum_score += float(student[i+5])
    
    avg_of_student_per_age_group[age - 17] += sum_score/count_score

# find the average score of each age group
for i in range(len(avg_of_student_per_age_group)):
    avg_of_student_per_age_group[i] = avg_of_student_per_age_group[i]/number_of_student_per_age_group[i]
    
for i in range(len(avg_of_student_per_age_group)):
    avg_of_student_per_age_group[i] = avg_of_student_per_age_group[i] * 70000 / 10

# plot bar chart
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()

# numpy list from 0-11
y_pos = np.arange(len(subjects))

# set limit
axis.set_ylim(0,70000)

age = ["17", "18", "19", "20", "21", "22", "23", "24", "25", "26", ">26"]

# plot the barchart using 2 list
plt.bar(y_pos, number_of_student_per_age_group, align='center', alpha=0.5)
plt.plot(y_pos, avg_of_student_per_age_group, color="red", marker="o")

# change horizontal category name 
plt.xticks(y_pos, age)

# lable and title 
plt.ylabel('Number of candidates')
plt.xlabel('Age')
plt.title('Average score by age group')

# right side ticks
ax2 = axis.twinx()
ax2.tick_params('y', colors="r")
ax2.set_ylim(0,10)
ax2.set_ylabel('Average score')

# make label on top of each bar
rects = axis.patches

for rect, label in zip(rects, number_of_student_per_age_group):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 2, label, ha="center", va="bottom")

plt.show()