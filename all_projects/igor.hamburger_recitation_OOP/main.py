''' OOP2 Exercise '''

from Student import Student
from Track import Track

############################################
# Test yourself - do not delete this comment
############################################

def q1():
    student1 = Student('John', 20, [55,100,70,88])
    student2 = Student('Mary', 22, [100,97,94,100])
    student3 = Student('Jane', 20, [47,60,77])
    print(student1)
    print(f'student1 grades are: {student1.get_grades()}')
    student1.add_grade(99)
    print(f'student1 grades are: {student1.get_grades()}')
    print(f'student2 lowest grade is {student2.lowest_grade()} and highest grade is {student2.highest_grade()}')
    print(f'The difference between {student1.name} and {student2.name} is {student1.grade_difference(student2)}')
    print(student1.introduce(student2, student3))

def q2():
    student1 = Student('John', 20, [55,100,70,88])
    student2 = Student('Mary', 22, [100,97,94,100])
    student3 = Student('Jane', 20, [47,60,77])
    student4 = Student('Joe', 19, [55,100,79,88, 99])
    t1 = Track('Math', 'Mr. Butterworth', [student1, student2, student3])
    print(t1)
    print(f'Math lowest average is {t1.lowest_avg()} and highest average is {t1.highest_avg()}')
    t1.add_student(student4)
    print(t1)
    t1.set_new_head('Mr. Frazer')
    print(t1)
    student5 = Student('Baber', 24, [60,97,94,100])
    student6 = Student('Ben', 21, [47,60,77])
    t2 = Track('Science', 'Mr. Frazer', [student5, student6])
    print(t2)
    print(f'The difference between {t1.get_subject()} and {t2.get_subject()} is {t1.grade_difference(t2)}')
    print(f'Track {t2.get_subject()} students are: {t2.get_students()}')
    
def q3():
    student1 = Student('John', 20, [55,100,70,88])

    # comment out the tests you don't want to run
    # you can only run one at the time
    #Invalid_s = Student(88, 20, [55,100,70,88])
    #Invalid_s = Student('Ben', '22', [55,100,70,88])
    #Invalid_s = Student('Ben', 22, [])
    #Invalid_s = Student('Ben', 22, [55,100,70,'88'])

    #Invalid_t = Track('Math', 'Mr. Butterworth', [33])
    #Invalid_t = Track('Math', 'Mr. Butterworth', [])
    #Invalid_t = Track(44, 'Mr. Butterworth', [student1])
    #Invalid_t = Track('Math', True, [student1])




if __name__ == '__main__':
    # comment out the questions you don't want to run
    q1()
    q2()
    #q3()