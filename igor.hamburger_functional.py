''' Python Functional Programming Exercise'''
import functools
import operator
from functools import reduce

#########################################
# Question 1 - do not delete this comment
# Iterators
#########################################
class PaliIter():
    '''
    An iterator that return palindroms from 0 to n (excluding n).
    '''

    def __init__(self, max: int):
        ''' Initialize the iterator. '''

        self._tail = max
        self.cur = 0

    def __iter__(self):
        ''' Return the iterator itself. '''

        return self

    def __next__(self):
        ''' Return the next palindrom. '''

        string_num = ''
        while self.cur < self._tail:
            string_num = str(self.cur)
            if string_num == string_num[::-1]:
                self.cur += 1
                return self.cur - 1
            else:
                self.cur += 1
        if self.cur >= self._tail:
            raise StopIteration

def q1(x):
    '''
    Print the 1'st, 20'th, 40'th and 100'th Palindromes (0 is the first).
    '''

    counter = 0
    for i in x:
        counter += 1
        if counter in [2, 21, 41, 101]:
            print(i)

#########################################
# Question 2 - do not delete this comment
# Generators
#########################################
def Palis(n):
    ''' 
    A generator that return palindroms from 0 to n (excluding n).
    '''

    str_num = ''
    for i in range(n):
        str_num = str(i)
        if str_num == str_num[::-1]:
            yield i

def q2(n):
    '''
    Print the 1'st, 20'th, 40'th and 100'th Palindromes (0 is the first).
    '''

    counter = 0
    for i in Palis(n):
        counter += 1
        if counter in [2, 21, 41, 101]:
            print(i)

#########################################
# Question 3 - do not delete this comment
# Functions and Lambdas
#########################################

# Solution 1 - using lambda
def compose(f, g): # -> function:
    ''' 
    Return a composition (function) of f and g (two functions).
    '''

    return lambda x: f(g(x))

# Solution 2 - using function definition
def compose2(f, g): # -> function:
    ''' 
    Return a composition (function) of f and g (two functions).
    '''

    return f(g)

def del_first_last(l: list[int]) -> list[int]:
    ''' 
    Return sub list of l without the first and last element.
    '''

    return l[1:-1]

def del_even(l: list[int]) -> list[int]:
    ''' 
    Return sub list of l without even numbers.
    '''

    return [x for x in l if x%2 != 0]


def q3(lst):
    '''
    Print the sub list of [1,2,3,4,5,6,7,8,9] without even numbers and without the first and last element.
    '''

    x = compose2(del_first_last, del_even(lst))
    print(x)

    y = compose(del_first_last, del_even) #using lambda function composition
    print(y(lst))


#########################################
# Question 4 - do not delete this comment
# Map, Filter and Reduce
#########################################

# Implement using map an Lambda
def break_down(sentence: str) -> list[str]:
    ''' 
    Return a list of lists of the form [w, w_in_upper, w_length].
    '''

    output_lst = list(map(lambda x: [x, x.upper(), len(x)], sentence.split()))
    return output_lst


def filter_length(l: list[str], n: int) -> list[str]:
    ''' 
    Return only the words that have a length of at least n.
    '''

    return list(filter(lambda x: len(x) >= n, l))


def flatten(l: list[set[int]]) -> set[int]:
    '''
    Return a set contains all elements of each set in l.
    '''

    return reduce(lambda x, y: set(x).union(set(y)), l) #option using union() function in two diferents sets every time

    lst = list(map(lambda x: list(x), l))
    output_set = set(functools.reduce(operator.iconcat, lst, []))
    return output_set

    return set(sum(lst, [])) #another option using sum function to flatten a nested list.


###################################
# Main - do not delete this comment
###################################

def q4():
    def q4_1():
        print(break_down('Hello world I like to code'))
    
    def q4_2():
        print(filter_length(['Hello', 'world', 'I', 'ye', 'no', 'Wohooo'], 3))
    
    def q4_3():
        print(flatten([{'a', 'b', 'c'}, {'a', 'd', 'c'}, {'a', 'b', 'e'}]))

    # comment out the questiones you don't want to run
    q4_1()
    q4_2()
    q4_3()

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    x = PaliIter(920)
    y = 920
    q1(x)
    q2(y)
    q3([1,2,3,4,5,6,7,8,9])
    q4()



















