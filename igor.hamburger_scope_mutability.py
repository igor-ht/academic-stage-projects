''' Python Scope, Aliasing,Tuples & Mutability Exercise '''

from ast import Return
from typing import Any, Union
from copy import deepcopy

#########################################
# Question 1 - do not delete this comment
#########################################
def assign(tup: tuple, i: int, value: Any) -> tuple:
    '''
    Return a new tuple with the value at index i replaced with value.
    '''
    #TODO: Write your code here

    tup_copy = tup[:i] + (value,) + tup[i+1:]
    return(tup_copy)

#########################################
# Question 2 - do not delete this comment
#########################################
def replace(tup: tuple, old_val: Any, new_val: any) -> tuple:
    '''
    Return a new tuple with all instances of old_val replaced with new_val.
    '''
    #TODO: Write your code here

    tup_new = ()
    for i in tup:
        if i != old_val:
            tup_new += (i,)
        else:
            tup_new += (new_val,)

    return tup_new

#########################################
# Question 3 - do not delete this comment
#########################################
def remove_empty(l: list[tuple]) -> list[tuple]:
    '''
    Return the list, without empty tuples.
    '''
    #TODO: Write your code here

    return [e for e in l if e != ()] #*** this is the most effective way of solving it, using list comprehension

    #empty_count = l.count(())

    #for i in range(empty_count):
    #    l.remove(())
    #return l

    #i = 0

    #for i in range(0, len(l) - 1):
    #    if len(l[i]) < 1:
    #        l.pop(i)
    #        i -= 1
    #    else:
    #        i += 1

    #for j in l:
    #    if len(j) < 1:
    #        l.remove(j)
    #        break
    #for i in l:
    #    if len(i) < 1:
    #        l.remove(j)
    #return l

#########################################
# Question 4 - do not delete this comment
#########################################
def str_to_tup(s: str) -> tuple:
    '''
    Return a tuple of the charachters in a string, excluding spaces.
    '''
    #TODO: Write your code here

    new_tup = ()

    for i in s:
        if i != ' ':
            new_tup += (i,)
    return new_tup

#########################################
# Question 5 - do not delete this comment
#########################################
def assign_complex(collection: Union[list, tuple], i: int, value: Any):
    '''
    Return a new collection with the value at index i replaced with value.
    If collection is not a list or tuple, return None.
    '''
    #TODO: Write your code here

    if type(collection) == tuple:
        collection == collection[:i] + (value,) + collection[i + 1:]
        return collection
    elif type(collection) == list:
        collection == collection[:i] + [value] + collection[i + 1:]
        return collection
    return None





###################################
# Main - do not delete this comment
###################################
def q1():
    x = assign( (0, 1, 2, 3, 4, 5), 3, 700)
    print(x)

    print('After modification:')
    y = ( [1, 2, 3], [4, 5, 6] )
    z = assign( y, 1, 'Changed' )
    y[0][0] = 1111
    print(y)
    print(z)

def q2():
    x = 1, 2, 7, 4, 4, 7, 3, 7, 8, 9
    x = replace(x, 7, 'BOOM')
    print(x)

    print('After modification:')
    y = ( [1, 2, 3], [4, 5, 6], [1, 2, 3] )
    z = replace(y, [1, 2, 3], 'Changed')
    y[1][0] = 1111
    print(y)
    print(z)

def q3():
    l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
    print(remove_empty(l))

def q4():
   print(str_to_tup('Hello World'))
   print(str_to_tup('I am a string'))

def q5():
    print(assign_complex(['a', 'b', 'c'], 1, 'Changed'))
    print(assign_complex(('a', 'b', 'c'), 1, 'Changed'))
    print(assign_complex({1, 3, 6}, 1, 'Changed'))

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    q3()
    #q4()
    #q5()
