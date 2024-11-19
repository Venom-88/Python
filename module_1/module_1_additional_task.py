grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]]
students = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'}

students_list = list(students)
students_list.sort()
average_grades = {}
for i in range(len(students_list)):
    student = students_list[i]
    grades_list = grades[i]
    average = sum(grades_list)/len(grades_list)
    average_grades[student] = average
print(average_grades)