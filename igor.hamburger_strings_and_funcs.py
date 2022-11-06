''' Python Strings and Loops Exercise'''

from typing import Union
import math

#########################################
# Question 1 - do not delete this comment
#########################################
def convert_spoon_to_cup(spoons: float) -> float:
    '''
    Convert spoons to cups with a ration of 3.5:1.
    Return a float with a precision of 2 decimal places.
    '''
    #TODO: Write your code here
    #spoons = float(input('How many spoons you want to convert to cups?'))
    cups = round(spoons / 3.5, 2)
    return cups
    #print('For', spoons, 'you will need', cups, 'cups.')

#########################################
# Question 2 - do not delete this comment
#########################################
def calculate_mathematical_expression(
    x: float,
    y: float,
    action: str) -> Union[float, None]:
    '''
    Calculate a mathematical expression with two numbers and an operator.
    '''
    #TODO: Write your code here

    if action == '+':
        ans = x + y
        #print('The answer for x + y is:', ans)
        return ans
    elif action == '-':
        ans = x - y
        #print('The answer for x - y is:', ans)
        return ans
    elif action == '/':
        if y == 0:
            return None
        ans = x / y
        #print('The answer for x / y is:', ans)
        return ans
    elif action == '*':
        ans = x * y
        #print('The answer for x * y is:', ans)
        return ans
    else:
        return None

#########################################
# Question 3 - do not delete this comment
#########################################
def calculate_from_string(str: str) -> Union[float, None]:
    '''
    Calculate a mathematical expression with two numbers and an operator based on a string.
    '''
    #TODO: Write your code here
    #for in in str:
    num1 = ''
    num2 = ''
    action = ''
    for i in str:
        num1 = num1 + i
        if i == ' ':
            break
    for j in range((len(str)-1),0,-1):
        num2 = str[j] + num2
        if str[j] == ' ':
            break
    for z in str:
        if z in '+,-,/,*':
            action = z
    x = int(num1)
    y = int(num2)

    return calculate_mathematical_expression(x,y,action)



#########################################
# Question 4 - do not delete this comment
#########################################
def largest_and_smallest(x: int, y: int, z: int) -> tuple[int, int]:
    '''
    Return the largest and smallest number from a list of numbers.
    '''
    #TODO: Write your code here
    big_num = 0
    small_num = 0

    if x >= y and x >= z:
        big_num = x
    elif y >= x and y >= z:
        big_num = y
    else:
        big_num = z

    if x <= y and x <= z:
        small_num = x
    elif y <= x and y <= z:
        small_num = y
    else:
        small_num = z
    return big_num, small_num

#########################################
# Question 5 - do not delete this comment
#########################################

def quadratic_equation(a: float, b: float, c: float) -> tuple[Union[float, None], Union[float, None]]:
    '''
    Solve a quadratic equation: ax**2 + bx + c = 0.
    '''
    #TODO: Write your code here
    x1 = (- b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x2 = (- b - ((b**2 - 4*a*c)**0.5))/(2*a)
    if x1 == x2:
        return x1, None
    elif type(x1) and type(x2) == complex:
        return None, None
    else:
        return x1, x2
#########################################
# Question 6 - do not delete this comment
#########################################
def quadratic_equation_user_input():
    '''
    Solve a quadratic equation: ax**2 + bx + c = 0 with user input.
    '''
    #TODO: Write your code here
    a,b,c = input('Insert coefficients a, b, and c:').split()

    x1, x2 = quadratic_equation(int(a), int(b), int(c))

    if x1 == x2:
        print(f'The equation has one solution: {x1}')
    elif type(x1) and type(x2) == complex:
        print(f'The equation has no solutions.')
    else:
        print(f'The equation has two solutions: {x1} and {x2}')


#########################################
# Question 7 - do not delete this comment
#########################################
def area_shape() -> Union[float, None]:
    '''
    Calculates the area of a shape with user input.
    Return a float with a precision of 2 decimal places.
    '''
    #TODO: Write your code here

    shape = input('Choose shape: 1=circle, 2=rectangle, 3=trapezoid.')

    if shape not in '123':
        return None

    if shape == '1':
        radius = int(input('How much is the radius?'))
        area = round(3.14 * ((float(radius))**2), 2)
        return area

    if shape == '2':
        s1, s2 = input('What are the height and widht sizes?').split()
        area = int(s1) * int(s2)
        return area

    if shape == '3':
        s1, s2, s3 = input('What are the first base, the second base and the height?').split()
        area = ((int(s1) + int(s2)) * int(s3)) / 2
        return area

###################################
# Main - do not delete this comment
###################################
def q1():
    print(convert_spoon_to_cup(7))
    print(convert_spoon_to_cup(10))


def q2():
    print(calculate_mathematical_expression(11, 8, "+"))
    print(calculate_mathematical_expression(10, 6, "-"))
    print(calculate_mathematical_expression(5, 6, "*"))
    print(calculate_mathematical_expression(5, 4, "/"))
    print(calculate_mathematical_expression(10, 2, "/"))
    print(calculate_mathematical_expression(5, 6, "^"))
    print(calculate_mathematical_expression(5, 0, "^"))


def q3():
    print(calculate_from_string("7 - 2"))
    print(calculate_from_string("2 * 7"))
    print(calculate_from_string("4 / 10"))
    print(calculate_from_string("10 / 0"))

def q4():
    print(largest_and_smallest(1, 5, 10))
    print(largest_and_smallest(10, 1, 5))
    print(largest_and_smallest(1, 1, 2))
    print(largest_and_smallest(0, 0, 0))

def q5():
    print(quadratic_equation(1, 1.5, -1))
    print(quadratic_equation(1, -8, 16))
    print(quadratic_equation(1, -2, 34.5))

def q6():
    quadratic_equation_user_input()

def q7():
    print(area_shape())

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    q7()