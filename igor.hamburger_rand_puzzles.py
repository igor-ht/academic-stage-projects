''' Python random and Puzzles Exercise'''

import random
import string


#################################################
# Question 1 - random- do not delete this comment
#################################################
def rand_str():
    '''
    Return random alphabetical string.
    String length is also random between 1 to 20.
    '''
    # TODO: write your code here

    num = random.randint(1, 20)
    source = string.ascii_letters
    the_word = ''
    for i in range(0, num):
        the_word += random.choice(source)
    return the_word


def rand_element(elements):
    '''
    Select a random element from a list, set, dictionary (value)
    Take care based on the type of the input.
    If the input type is not compatible, print an error message and return None
    '''
    # TODO: write your code here

    if type(elements) == list:
        return random.choice(elements)
    elif type(elements) == set:
        return random.choice(list(elements))
    elif isinstance(elements, dict):
        return random.choice(list(elements.values()))
    raise ValueError (f'input {elements} of type class {type(elements)} is not compatible')

###################################################
# Question 2 - Puzzles - do not delete this comment
###################################################
def upper_even_idx(s):
    ''' 
    Returns a list of the positions of all uppercase vowels in even indices of a given string.
    '''
    # TODO: write your code here
    new_lst = []
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] in 'aeiouAEIOU':
                if s[i].isupper():
                    new_lst.append(i)
    return new_lst

def sum_big_first_k(nums, k):
    ''' 
    Returns the sum of the numbers of a given list among the first k elements with more than 2 digits.
    '''
    # TODO: write your code here

    total_sum = 0
    for n in range(k):
        if nums[n] >= 100:
            total_sum += nums[n]

    return total_sum

def get_valid_files(file_names):
    ''' 
    Returns a sub list with files with a valid name.
    A valid filename should end in .txt, .exe, .jpg, or .png, should start with an alphabetic char
    and have at most three digits.
    '''
    # TODO: write your code here

    files_options = ['.txt', '.exe', '.jpg', '.png']
    new_files_lst = []
    for files in file_names:
        for end in files_options:
            if end in files:
                count = 0
                for number in files:
                    if number in '0123456789':
                        count += 1
                if count <= 3:
                    if files[0].islower():
                        new_files_lst.append(files)
    return new_files_lst


###################################
# Main - do not delete this comment
###################################
def q1():
    print('Q1 - random:')
    print(f'Random string: \"{rand_str()}\"')

    l = ['hi', 'hello', 'bye', 'goodbye']
    s = set(['banana', 'apple', 'orange'])
    d = {'key1': 1, 'key2': 2, 'key3': 3}
    print(f'Random element from list: {rand_element(l)}')
    print(f'Random element from set: {rand_element(s)}')
    print(f'Random element from dict: {rand_element(d)}')
    rand_element(4)


def q2():
    print('Q2 - Puzzles:')

    def test_upper_even_idx():
        print(f'Upper case vowels in even indices:')
        print(f'\"Hello World\": {upper_even_idx("Hello World")}')
        print(f'\"BYE BYE MAN\": {upper_even_idx("BYE BYE MAN")}')
        print()

    def test_sum_big_first_k():
        print(f'Sum of elements with more then 2 digits from first k')
        l1 = [5, 17, 9, 108, -9, 300, 76]
        k1 = 2
        print(f'For input {l1} with K={k1} is: {sum_big_first_k(l1, k1)}')
        k2 = 4
        print(f'For input {l1} with K={k2} is: {sum_big_first_k(l1, k2)}')
        k3 = 6
        print(f'For input {l1} with K={k3} is: {sum_big_first_k(l1, k3)}')
        print()

    def test_get_valid_files():
        print(f'Valid files:')
        files1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
        print(f'Input: {files1}, output: {get_valid_files(files1)}')

        files1 = ['a12344.txt', '.png', '3file.jpg', 'win32.exe']
        print(f'Input: {files1}, output: {get_valid_files(files1)}')
        print()

    # comment out the questiones you don't want to run
    #test_upper_even_idx()
    #test_sum_big_first_k()
    test_get_valid_files()


if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    q2()
