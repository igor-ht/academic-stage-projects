''' Command Line Arguments Exercise'''

import sys

#########################################
# Question 1 - do not delete this comment
#########################################
def prog_call():
    '''
    Indicate the user that the program was called.
    If the user provided additional arguments to the command, inform him about the wrong usage and list them. 
    '''
    #TODO: add your code here
    import sys

    print_call()

    if len(sys.argv) > 2:
        for i in range(2, len(sys.argv)):
            print(f'This commands expect no arguments, but the following were given:\nArgument {i} was "{sys.argv[i]}"')


#########################################
# Question 2 - do not delete this comment
#########################################
def shopping_list():
    '''
    Creates and print a shopping list from the command line arguments.
    No replications are allowed.
    Hint: think about which data structure you need to use.
    If the user haven't provided additional arguments to the command, inform him about the wrong usage.
    '''
    #TODO: add your code here

    print_call()
    s = []
    if len(sys.argv) <= 2:
        print(f'Expects at least one more argument, but none were given.')
    else:
        print(f'This is the shopping list:')
        for i in range(2, len(sys.argv)):
            if sys.argv[i] not in s:
                s.append(sys.argv[i])
        for l in s:
            print(l)


#########################################
# Questions 3 - do not delete this comment
#########################################
def bd_dict():
    '''
    Creates and print a birthday dictionary from the command line arguments.
    If the user haven't provided additional arguments to the command, inform him about the wrong usage.
    Make sure the input is of the structure [<name> <bool> <name> <bool> ...]
    Name can be anything for now...
    '''
    #TODO: add your code here

    if len(sys.argv) <= 2:
        print(f'Expects at least one more argument, but none were given.')
        return
    elif len(sys.argv) % 2 != 0:
        print(f'Expects at least two arguments: <name> <bool>, but only one was given.')
        return

    dic = {}
    name_lst = sys.argv[2::2]
    bool_lst = sys.argv[3::2]
    for i in range(len(name_lst)):
        if len(name_lst) != len(bool_lst):
            print(f'Expects an even number of arguments: <name> <bool>, but an odd number was given.')
        elif bool_lst[i] == 'True':
            dic[name_lst[i]] = True
        elif bool_lst[i] == 'False':
            dic[name_lst[i]] = False
        else:
            print(f"Expects a boolean value, but \"{bool_lst[i]}\" was given")
            return

    print(f'This is the birthday dictionary:')

    print(dic)
    return

#########################################
# Questions 4 - do not delete this comment
#########################################

def full_program():
    '''
    Enables the user to use all the 3 functions in this file.
    Detect which function the user wants to use by the first command line argument.
    '''
    #TODO: add your code here
    if len(sys.argv) < 2:
        print(f'Program command_line_arg.py was called, but no command was given.')
        return
    elif sys.argv[1] == 'PROG_CALL':
        return prog_call()
    elif sys.argv[1] == 'SHOPPING_LIST':
        return shopping_list()
    elif sys.argv[1] == 'BD_DICT':
        return bd_dict()

    else:
        print(f'Program command_line_arg.py was called, but the command: {sys.argv[1]} is not recognized')
    return
###############################################
# Helper Functions - do not delete this comment
###############################################
#TODO: add your code here, if you want
def print_call():
    print(f'The program {sys.argv[0]} was called, the command was "{sys.argv[1]}"')

###################################
# Main - do not delete this comment
###################################
if __name__ == '__main__':
    # comment out the functions you don't want to use
    #prog_call()
    #shopping_list()
    #bd_dict()
    full_program()