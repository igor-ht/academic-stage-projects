''' Python Dictionaries, Sets, and Comprehension Exercise '''
import copy
from typing import Any

#########################################
# Question 1 - do not delete this comment
#########################################

def most_popular_digit(num: int) -> int:
    '''
    Returns the most popular digit in a positive integer.
    In case of 2 or more most popular digits, returns the biggest one.
    '''
    #TODO: Write your code here

    counter = 0
    not_num = str(num)
    popular = ''

    for n in not_num:
        c = not_num.count(n)
        if c > counter:
            counter = c
            popular = n
        elif c == counter:
            if n > popular:
                popular = n

    return int(popular)



#########################################
# Question 2 - do not delete this comment
#########################################
def courses_per_student(l: list[tuple[str, str]]) -> dict[str, list[str]]:
    '''
    Takes a list of tuples with the format: (<name>, <course_name>).
    If a student takes more than one course, his name will appear in several tuples.
    Returns a dictionary with the format: {<name>: [<course_name1>, <course_name1>, ...]}
    '''
    #TODO: Write your code here

    dic_names = {}

    for i in l:
        n = ''
        course = []
        n = i[0].lower()
        course.append(i[1].lower())
        if n not in dic_names:
            dic_names[n] = course
        elif course[0] not in dic_names[n]:
            dic_names[n] += course

    return dic_names


#########################################
# Question 3 - do not delete this comment
#########################################
def hours_per_student(student_course: dict[str, list[str]], course_hours: dict[str, int]) -> dict[str, int]:
    '''
    Takes a dictionary of students and courses they take and a dictionary of courses and their hours
    Returns a dictionary that maps every student to the sum of hours of his courses
    '''
    #TODO: Write your code here

    dic_sum = {}

    for n in student_course.keys():
        dic_sum[n] = 0
        for course in student_course[n]:
            dic_sum[n] += course_hours[course]

    return dic_sum



#########################################
# Question 4 - do not delete this comment
#########################################
def swap_students_courses(student_course: dict[str, list[str]]) -> dict[str, list[str]]:
    '''
    Takes a dictionary of students and their courses.
    Returns a dictionary of courses and their participants.
    '''
    #TODO: Write your code here


    courses = {}
    for student in student_course.keys():
        for course in student_course[student]:
            if course not in courses.keys():
                courses[course] = [student]
            elif student not in courses[course]:
                courses[course].append(student)
    return courses


#########################################
# Question 5 - do not delete this comment
#########################################
def map_keys_to_values(k_lst: list, v_lst: list) -> dict[Any, Any]:
    '''
    Takes 2 lists of equal length.
    Returns a dictionary with the format: {<k_lst[i]>: <v_lst[i]>, ...}
    If a key appears in k_lst more than once, the value will be the last one in v_lst.
    '''
    #TODO: Write your code here

    dic = {}
    for k in range(len(k_lst)):
        dic[k_lst[k]] = v_lst[k]
    return dic




#########################################
# Question 6 - do not delete this comment
#########################################
def map_keys_to_values_list(k_lst: list, v_lst: list) -> dict[Any, list]:
    '''
    Takes 2 lists of equal length.
    Returns a dictionary with the format: {<k_lst[i]>: [<v_lst[i]>, <v_lst[j]> ...]}, 
    where i, j, ... are the indexies where k_lst[i] appears in k_lst.
    '''
    #TODO: Write your code here
    new_dic = {}

    for i in range(len(k_lst)):
        if k_lst[i] not in new_dic.keys():
            new_dic[k_lst[i]] = [v_lst[i]]
        else:
            new_dic[k_lst[i]].append(v_lst[i])

    return new_dic

#########################################
# Question 7 - do not delete this comment
#########################################
def append_to_unique_list(unique_lst: list[int], element: int) -> list[int]:
    '''
    Takes a list of unique elements and an element.
    Returns a list with the element appended to the list if it is not already in the list.
    '''
    #TODO: Write your code here

    if element not in unique_lst:
        unique_lst.append(element)

    return unique_lst


#########################################
# Question 8 - do not delete this comment
#########################################
def map_keys_to_values_ulist(k_lst, v_lst):
    '''
    Takes 2 lists of equal length.
    Returns a dictionary with the format: {<k_lst[i]>: [<v_lst[i]>, <v_lst[j]> ...]},
    where i, j, ... are the indexies where k_lst[i] appears in k_lst,
    and [<v_lst[i]>, <v_lst[j]> ...] is a unique list.
    '''
    #TODO: Write your code here
    new_dic = {}

    for i in range(len(k_lst)):
        if k_lst[i] not in new_dic:
            new_dic[k_lst[i]] = [v_lst[i]]
        else:
            append_to_unique_list(new_dic[k_lst[i]], v_lst[i])
    return new_dic

###################################
# Main - do not delete this comment
###################################
def q1():
    print(most_popular_digit(138631))
    print(most_popular_digit(11000))

def q2():
    l = [("Rina", "Math"), ("Yossi", "biologY"), ("Riki", "python"), ("Rina", "pYthon"), ("Yossi", "biology")]
    print(courses_per_student(l))


def q3():
    student_course = {'rina' : ['math', 'python'], 'yossi' :['chemistry', 'biology'], 'riki' : ['python'], 'shlomi' : []}
    course_hours = {'math' : 4, 'python' : 4, 'chemistry' : 6,'biology' : 5}
    print(hours_per_student(student_course, course_hours))

def q4():
    print(swap_students_courses({'rina': ['math', 'python'], 'yossi': ['chemistry', 'biology'], 'riki': ['python']}))
    print(swap_students_courses({'rina': ['math', 'math'], 'yossi': ['chemistry', 'biology'], 'riki': ['python']}))

def q5():
    print(map_keys_to_values(["a", "b", "c"], [15, 1, 2]))
    print(map_keys_to_values(["a", "b", "a"], [15, 1, 6]))

def q6():
    print(map_keys_to_values_list(["a", "b", "a"], [15, 3, 6]))
    print(map_keys_to_values_list(["a", "c", "a", "a"], [15, 3, 6, 15]))

def q7():
    lst = []
    append_to_unique_list(lst, 44)
    print(lst)
    append_to_unique_list(lst, 3)
    print(lst)
    append_to_unique_list(lst, 3)
    print(lst)

def q8():
    print(map_keys_to_values_ulist(["hi", "a", "c", "a", "a", "c", "hi"], [1, 15, 3, 6, 15, 3, 2]))
    print(map_keys_to_values_ulist(["b", "b", "b", "b", "b"], [15, 17, 17, 15, 3]))

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()
    q8()