''' Python Basic Recap Exercise'''

#########################################
# Question 1 - do not delete this comment
#########################################
def first():
    '''
    First Python application!
    '''
    #TODO: Write your code here
    print("|-----------------------------|")
    print("|                             |")
    print("| My first Python application!|")
    print("|                             |")
    print("|-----------------------------|")

#########################################
# Question 2 - do not delete this comment
#########################################
def variables():
    '''
    Working with variables.
    '''
    #TODO: Write your code here

    x = 1
    y = 2
    pi = 3.14
    boolean = "False"
    print(x)
    print(y)
    print(pi)
    print(boolean)

#########################################
# Question 3 - do not delete this comment
#########################################
def intro():
    '''
    Print self introduction.
    '''
    #TODO: Write your code here

    name = "Igor"
    birth_year = 1993
    height = 1.70
    print("Hi, my name is", name)
    print("I was born in", birth_year)
    print("I am", height, "meters tall.")

#########################################
# Question 4 - do not delete this comment
#########################################
def print_digits():
    '''
    Print the digits of a number seperately.
    The number is entered as an input and can be between 10 and 99.
    '''
    #TODO: Write your code here

    num = int(input('Enter a number between 10 and 99:'))
    if num in range(10,100):
        tens = num // 10
        unit = num % 10
        print("Unit:", unit)
        print("Tens:", tens)
    else:
        print("Input not valid.")

#########################################
# Question 5 - do not delete this comment
#########################################
def average():
    '''
    Calculate the average of three of numbers and print the result.
    '''
    #TODO: Write your code here

    first = 10
    second = 20
    third = 3
    avg = (first+second+third)//3
    print(avg)

#########################################
# Question 6 - do not delete this comment
#########################################
def sum_digits():
    '''
    Calculate the sum of digits of a 4-digits number and print the result.
    '''
    #TODO: Write your code here

    num = int(input('Enter a four digit number:'))
    num_new = 0
    x1 = num // 1000
    num_new = num - (x1 * 1000)
    x2 = num_new // 100
    num_new = num_new - (x2 * 100)
    x3 = num_new // 10
    num_new = num_new - (x3 * 10)
    x4 = num_new
    sum = x1+x2+x3+x4
    print(sum)


#########################################
# Question 6 - do not delete this comment
#########################################
def sec_to_time():
    '''
    Calculate the sum of digits of a 4-digits number and print the result.
    '''
    #TODO: Write your code here

    sec_time = 0
    min_time = 0
    hour_time = 0
    seconds = int(input('Enter a number:'))
    if seconds >= 60:
        min_time = (seconds//60)
        sec_time = (seconds % 60)
        if min_time >= 60:
            hour_time = (min_time//60)
            min_time = (min_time % 60)

    print(hour_time, ":", min_time, ":", sec_time)

###################################
# Main - do not delete this comment
###################################
def q1():
    first()


def q2():
    variables()

def q3():
    intro()

def q4():
    print_digits()

def q5():
    average()

def q6():
    sum_digits()

def q7():
    sec_to_time()

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()