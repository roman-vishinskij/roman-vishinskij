grades = [[5, 3, 3, 5, 4], [2, 2, 2,3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4,5]]
students = {'Johnny', 'Bibo', 'Steve', 'Khendrik', 'Aaron'}
students_list_1 = sorted(students)
grades_list = 0
students_list = 0
for i in students:
    print(students_list_1[students_list], ':', ((sum(grades[grades_list ]) / len(grades[grades_list]))))
    grades_list += 1
    students_list += 1


