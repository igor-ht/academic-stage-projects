import copy


#Question 1:
class PersonNode:
    def __init__(self, name, age, prev=None, next = None):
        self.name = name
        self.age = age
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'Name: {self.name}, age: {self.age}'


#Question 2:
class PersonList:

    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail
        self.__size = 0

    def __repr__(self):
        cur = self.__head
        while cur.next != None:
            print(f'{cur}')
            cur = cur.next
        return str(self.__tail)


    def add(self, name, age):
        new_person = PersonNode(name, age)
        if self.__head == None:
            self.__head = new_person
            self.__size += 1
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = new_person
            new_person.prev = cur
            self.__size += 1
            self.__tail = new_person

    def list_length(self):
        #return self.__size
        if self.__head == None:
            return 0
        else:
            cur = PersonList(self.__head.next)
            return 1 + cur.list_length()

    def copy_list(self):
        if self.__head == None:
            return None
        elif self.__head.next == None:
            return str(copy.deepcopy(self.__head))
        cur = copy.deepcopy(self.__head)
        while cur.next != None:
            print(f'{cur}')
            cur = copy.deepcopy(cur.next)
        return str(copy.deepcopy(self.__tail))










