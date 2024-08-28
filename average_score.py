grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(students)
average_grades = {}
for i in range(len(student_list)):
    student = student_list[i]
    grades_for_student = grades[i]
    average = sum(grades_for_student) / len(grades_for_student)
    average_grades[student] = average
print(average_grades)