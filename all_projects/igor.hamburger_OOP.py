''' OOP2 Exercise '''

#########################################
# Question 2 - do not delete this comment
#########################################

from Student import Student

class Track:
    ''' Represent a track. '''

    def __init__(self, subject: str, head: str, students: list[Student]):
        ''' Constructor for a Track object. '''
        #TODO: write your code here
        self.subject = subject
        self.head = head
        self.students = students
        if len(self.students) < 1:
            raise TypeError ('Invalid input')
    
    def get_subject(self):
        ''' Return the track's subject. '''
        #TODO: write your code here
        return self.subject

    def get_num_students(self):
        ''' Return the number of students. '''
        #TODO: write your code here
        return len(self.students)
    
    def get_students(self):
        ''' Return the list of the students. '''
        #TODO: write your code here
        lst_students = []
        for s in self.students:
            lst_students.append(s.name)
        return lst_students
    
    def get_track_head(self):
        ''' Return the name of the head of the track. '''
        #TODO: write your code here
        return self.head

    def average_grade(self):
        ''' Return the average of track (2 digits after the decimal point). '''
        #TODO: write your code here
        total_grade = 0
        for s in self.students:
            total_grade += s.average_grade()
        return '%.2f' % (total_grade / len(self.students))


    def add_student(self, student: Student):
        ''' Add a new student. '''
        #TODO: write your code here
        return self.students.append(student)
    
    def lowest_avg(self):
        ''' Return the lowest average. '''
        #TODO: write your code here
        total_grade = []
        for s in self.students:
            total_grade.append(float('%.2f' % (s.average_grade())))
        return min(total_grade)
    
    def highest_avg(self):
        ''' Return the highest average. '''
        #TODO: write your code here
        total_grade = []
        for s in self.students:
            total_grade.append(float('%.2f' % (s.average_grade())))
        return max(total_grade)
    
    def set_new_head(self, new_head: str):
        ''' Sets a new head for the track. '''
        #TODO: write your code here
        self.head = new_head
        return self.head
    
    def __str__(self):
        ''' Return a string representation of the track. '''
        #TODO: write your code here
        return f'Track {self.subject} of {self.head} has {self.get_num_students()} and an average of {self.average_grade()}'
    
    def grade_difference(self, other):
        '''
        Return the difference between the average of this track and another track
        (2 digits after the decimal point). 
        '''
        #TODO: write your code here
        grade1 = float(self.average_grade())
        grade2 = float(other.average_grade())
        return '%.2f' % (grade1 - grade2)