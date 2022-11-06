''' OOP2 Exercise '''

#########################################
# Question 1 - do not delete this comment
#########################################

class Student:
    ''' Represent a student '''

    def __init__(self, name: str, age: float, grades: list[float]):
        ''' Constructor for a Student object. '''
        #TODO: write your code here
        if type(name) != str:
            raise TypeError('invalid input')
        elif type(age) != int:
            raise TypeError('invalid input')
        elif len(grades) < 1:
            raise TypeError('Invalid input')
        self.name = name
        self.age = age
        self.grades = grades
        for g in self.grades:
            if type(g) != int:
                raise TypeError('invalid input')


    
    def get_name(self):
        ''' Return the name of the student. '''
        #TODO: write your code here
        return self.name
    
    def num_grades(self):
        ''' Return the number of grades. '''
        #TODO: write your code here
        return len(self.grades)
    
    def get_grades(self):
        ''' Return the list of the grades. '''
        #TODO: write your code here
        return self.grades

    def average_grade(self):
        ''' Return the average of the grades (2 digits after the decimal point). '''
        #TODO: write your code here
        return round(sum(self.grades) / self.num_grades(), 2)
    
    def add_grade(self, grade: float):
        ''' Add a new grade to the list of grades. '''
        #TODO: write your code here
        return self.grades.append(grade)
    
    def lowest_grade(self):
        ''' Return the lowest grade. '''
        #TODO: write your code here
        return min(self.grades)
    
    def highest_grade(self):
        ''' Return the highest grade. '''
        #TODO: write your code here
        return max(self.grades)
    
    def __str__(self):
        ''' Return a string representation of the student. '''
        #TODO: write your code here
        return f'Student {self.name} is age {self.age}, and has an average of {self.average_grade()}'
    
    def grade_difference(self, other):
        ''' 
        Return the difference between the average of this student's grades another student's grades
        (2 digits after the decimal point).    
        '''
        #TODO: write your code here
        return '%.2f' % (self.average_grade() - other.average_grade())

    def introduce(self, other1, other2):
        ''' Prints an introduction this student make between two other students. '''
        #TODO: write your code here
        return f'Hello {other1.name}, let me introduce you to {other2.name}'