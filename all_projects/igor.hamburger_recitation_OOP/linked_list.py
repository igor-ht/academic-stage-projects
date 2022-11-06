
#1 question:
class PersonNode:
    def __init__(self, name, age, next = None):
        self.name = name
        self.age = age
        self.next = next

    def __repr__(self):
        return str(self.name), str(self.age)



#2 question:
class PersonList:

    def __init__(self, head = None):
        self.__head = head


    #def __repr__(self):
        #return str(self.__head)

    def add_person(self, name, age):
        new_person = PersonNode(name, age, None)
        cur = self.__head
        if cur.next != None:
            cur = cur.next
        else:
            cur.next = new_person

    def list_lenght(self):
        cur = self.__head
        if cur == None:
            return 0
        else:
            return 1 + self.list_lenght(cur.next)

    def copy_lst(self):
        copy_lst = []
        cur = self.__head
        while cur.next != None:
            copy_lst.append(cur)
            cur = cur.next
        return copy_lst

    







