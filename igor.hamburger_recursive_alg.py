''' Python Recursion Algorithms Implementation Exercise '''
import copy


#########################################
# Question 1 - do not delete this comment
#########################################
def gcd(a: int, b: int) -> int:
    ''''
    Returns the GCD of a, b.
    '''
    #TODO: Write your code here
    if b <= 1:
        return b
    if a % b == 0:
        return b
    return gcd(b, a % b)


#########################################
# Question 2 - do not delete this comment
#########################################
def selection_sort_slicing(l: list[int]) -> list[int]:
    '''
    Returns a sorted version of l, using slicing.
    '''
    #TODO: Write your code here
    if len(l) == 0:
        return []
    for n in range(len(l)-1):
        if l[0] > l[n+1]:
            l[0], l[n+1] = l[n+1], l[0]
    return [l[0]] + selection_sort_slicing(l[1:])


def indx_runner(l, indx): #help function for selection_sort_ruinning_i
    if indx >= len(l)-1:
        return []
    for n in range(indx, len(l)):
        if l[n] < l[indx]:
            l[indx], l[n] = l[n], l[indx]
    return [l[indx]] + indx_runner(l, indx+1)

def selection_sort_running_i(l: list[int]) -> list[int]:
    '''
    Returns a sorted version of l, using a running index
    '''
    #TODO: Write your code here

    return indx_runner(l, 0) #using the help of a recursive function that sorts a list using a index runner

    #s_lst = []
    #copy_lst = copy.copy(l)
    #while len(copy_lst) != 0:
    #    min_num = float('inf')
    #    for s in copy_lst:
    #        if s <= min_num:
    #            min_num = s
    #    s_lst.append(min_num)
    #    copy_lst.remove(min_num)
    #return s_lst #brute force function

#########################################
# Question 3 - do not delete this comment
#########################################
def bin_indx_search(lst, value, left, right, middle):

    while left <= right:
        if value == lst[middle]:
            return middle
        elif value < lst[middle]:
            return bin_indx_search(lst, value, left, middle-1, (left+middle)//2)
        elif value > lst[middle]:
            return bin_indx_search(lst, value, middle+1, right, (right+middle)//2)
    return -1

def bin_search(lst: list[int], val: int) -> int:
    '''
    Returns the index of val in lst. if it's not in lst, returns -1.
    Assumes lst is sorted.
    '''
    #TODO: Write your code here

    #option using the recursive function bin_indx_search
    return bin_indx_search(lst, val, 0, len(lst), 0+len(lst)//2)

    #option using the statement that the list is in range(1, 11) and sorted
    #return val-1 if val in lst else -1


###################################
# Main - do not delete this comment
###################################
def q1():
    print(f'The GCD of 34 and 10 is {gcd(34, 10)}')
    print(f'The GCD of 78 and 182 is {gcd(78, 182)}')
    print(f'The GCD of 20 and 30 is {gcd(20, 30)}')
    print(f'The GCD of 100 and 100 is {gcd(100, 100)}')
    print(f'The GCD of 600 and 500 is {gcd(600, 500)}')
    print(f'The GCD of 3 and 9 is {gcd(3, 9)}')

def q2():
    lst1 = [3, 4, 5, 1, 2, 8, 3, 7, 6]
    lst2 = [3, 4, 5, 1, 2, 8, 3, 7, 6, 900000, -9]
    print(f'List 1: {lst1}')
    print(f'List 2: {lst2}')
    print('Slicing:')
    print(f'List 1 sorted: {selection_sort_slicing(lst1)}')
    print(f'List 2 sorted: {selection_sort_slicing(lst2)}')
    print('Running index:')
    print(f'List 1 sorted: {selection_sort_running_i(lst1)}')
    print(f'List 2 sorted: {selection_sort_running_i(lst2)}')

def q3():
    print(f'Binary search of 3 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is {bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)}')
    print(f'Binary search of 7 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is {bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)}')
    print(f'Binary search of 10 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is {bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)}')
    print(f'Binary search of 0 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is {bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)}')
    print(f'Binary search of -1 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is {bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1)}')

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    q1()
    q2()
    q3()