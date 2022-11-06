''' Python Linked List Exercise Test '''

from linked_list import PersonNode, PersonList #, contains_loop

###################################
# Main - do not delete this comment
###################################
def q1():
    node = PersonNode("John", 30)
    print(node)

def q2():
    l = PersonList()
    l.add("John", 30)
    l.add("Jane", 25)
    l.add("Joe", 20)
    print(l)
    print(l.list_length())
    print('Copy list:')
    print(l.copy_list())

def q4():
    l = PersonList()
    l.add("John", 30)
    l.add("Jane", 25)
    l.print_line()

    print('Calling add_israeli, adding Joe:')
    l.add_israeli("Joe", 20)
    l.print_line()
    
    print('Removing Joe:')
    l.remove("Joe")
    l.print_line()

    print('Adding VIP:')
    l.add_VIP("VIP", 100)
    l.print_line()

    print('is_in_list("VIP"):' , l.is_in_line("VIP"))

    print('Reverse list:')
    l.reverse_list()
    l.print_line()

def q5():
    l = PersonList()
    print(f'contains_loop on an empty list: {contains_loop(l)}')
    l.add("John", 30)
    l.add("Jane", 25)
    l.add("Joe", 20)
    l.add("VIP", 100)
    l.print_line()
    print(f'contains_loop: {contains_loop(l)}')

    print('Adding loop...')
    l.head.nextNode.nextNode.nextNode = l.head
    print(f'contains_loop: {contains_loop(l)}')

    print()
    print('List of one element that points to itself:')

    l2 = PersonList()
    l2.add("John", 30)
    l2.print_line()
    l2.head.nextNode = l2.head
    print(f'contains_loop: {contains_loop(l2)}')

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    q2()
    #q4()
    # q5()