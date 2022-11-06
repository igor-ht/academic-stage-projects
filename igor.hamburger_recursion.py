''' Python Recursion Exercise'''
import copy


#########################################
# Question 1 - do not delete this comment
#########################################

def mult(x: int, y: int) -> int:
    '''
    Return the product of x and y.
    '''
    #TODO: insert your code here

    if y == 0:
        return 0


    return x + mult(x, y - 1)

#########################################
# Question 2 - do not delete this comment
#########################################

def rec_sum(a_1: int, d: int, n: int) -> int:
    '''
    Return the sum of the first n terms of the arithmetic sequence defined by a_1, d.
    '''
    #TODO: insert your code here

    if n == 1:
        return a_1


    return a_1 + rec_sum(a_1 + d, d, n-1)

    #return a_1 + d * (n - 1) + rec_sum(a_1, d, n - 1)

#########################################
# Question 3 - do not delete this comment
#########################################
def find_max_modulo(numbers: list[int], m: int) -> int:
    '''
    Return the largest number in the list that is a multiple of m.
    If no such number exists, return -1.
    '''
    #TODO: insert your code here

    numbers = sorted(numbers)

    if len(numbers) == 0:
        return -1

    if numbers[-1] % m == 0:
        return numbers[-1]
    else:
        numbers = numbers[0:(len(numbers)-1)]
        return find_max_modulo(numbers, m)






#########################################
# Question 4 - do not delete this comment
#########################################
def pay(b1: int, b2: int, m: int) -> bool:
    '''
    Return True if m can be payed using b1,b2 coins and False otherwise.
    Return False if m is negative.
    '''
    #TODO: insert your code here
    if m < 0:
        return False
    if m == 0:
        return True

    return pay(b1, b2, m - b1) or pay(b1, b2, m - b2)

#########################################
# Question 5 - do not delete this comment
#########################################
def pay_limit(b1: int, b2: int, c1: int, c2: int, m: int, total_bits: int) -> bool:
    '''
    Return True if m can be payed using b1,b2 coins and False otherwise, with constraints on the cost.
    Return False if m is negative or total_bits is negative.
    '''
    #TODO: insert your code here
    if m < 0 or total_bits < 0:
        return False
    if b1 + b2 == m and c1 + c2 <= total_bits:
        return True
    return pay_limit(b1, b2, c1, c2, m - b1, total_bits - c1) or pay_limit(b1, b2, c1, c2, m - b2, total_bits - c2)

#################
# Question 6 - do not delete this comment
#########################################

# Note that we didn't type this function because it can get and return any variable type.
# We could have typed it as:
# def deepcopy_list(lst: Any) -> Any:
def deepcopy_list(lst):
    '''
    Return a deep copy of the list.
    '''
    #TODO: insert your code here

    if len(lst) == 0:
        return None
    return copy.deepcopy(lst)

###################################
# Main - do not delete this comment
###################################
def q1():
    print(mult(9, 4))
    print(mult(9, 0))

def q2():
    print(rec_sum(2, 2, 5))
    print(rec_sum(2, 2, 1))
    print(rec_sum(1, 3, 4))

def q3():
    print(find_max_modulo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(find_max_modulo([1, 2, 9, 10], 5))
    print(find_max_modulo([1, 2, 9], 5))

def q4():
    print(pay(1, 2, 3))
    print(pay(2, 4, 11))
    print(pay(2, 5, -4))


def q5():
    print(pay_limit(1, 2, 1, 1, 3, 3))
    print(pay_limit(2, 4, 1, 1, 10, 2))
    print(pay_limit(1, 2, 1, 1, -1, 2))

def q6():
    print(deepcopy_list([1, 2, 3, 4, 5]))
    print(deepcopy_list([1, 2, [3], [[1, 2, 3]], [10, 11], 5]))

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    #q3()
    q4()
    #q5()
    #q6()
