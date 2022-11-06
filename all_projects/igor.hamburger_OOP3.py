''' Python OOP3 - Inheretance Exercise '''

from typing import Union

# Constants
BOT_SATISFACTION = 1.0
TOP_SATISFACTION = 5.0
BOT_CLEAN_LEVEL = 1
TOP_CLEAN_LEVEL = 10
BASIC_RANK = 1
STANDARD_RANK = 2
LUXURY_RANK = 3

class RoomError(Exception):
    # A subclass of Exception that defines a new error type
    # DO NOT change this class
    pass

#########################################
# Question 1 - do not delete this comment
#########################################

class Room:
    ''' Represents a room '''
    def  __init__(
        self,
        floor: int,
        number: int,
        clean_level: int,
        rank: int,
        satisfaction: Union[int, float] = 1.0,
        guests: list[str] = []):
        ''' Constructor of a room object ''' 
        #TODO: write your code here
        self.floor = floor
        self.number = number
        self.guests = [str.lower(name) for name in guests]
        try:
            if type(clean_level) == int:
                self.clean_level = clean_level
            if type(rank) == int:
                self.rank = rank
            if type(satisfaction) == int or type(satisfaction) == float:
                self.satisfaction = satisfaction
        except TypeError:
            print(f'One or more of the input is not from the right type.')

        try:
            if self.clean_level > 0 and self.clean_level < 11:
                pass
            if self.rank > 0 and self.rank < 4:
                pass
            if self.satisfaction > 0 and self.satisfaction < 6:
                pass
        except ValueError:
            print(f'One or more of the input is not valid.')

    def __repr__(self) -> str:
        ''' Returns a string representation of the room '''
        #TODO: write your code here
        #self.guests = list(sum(self.guests, []))
        return f'floor: {self.floor}\nroom: {self.number}\nguests: {", ".join(self.guests)}\nclean level: {self.clean_level}\nrank: {self.rank}\nsatisfaction: {self.satisfaction}\ntype: {self.__class__.__name__}'

    def is_occupied(self):
        ''' Returns True if the room is occupied '''
        #TODO: write your code here
        return len(self.guests) > 0

    def can_clean(self) -> bool:
        ''' Returns True if the room can be cleaned '''
        # default implementation
        return True

    def clean(self):
        '''
        Cleans the room.
        Raises a RoomError if the room is not cleanable.
        Perform one cleaning step, that is update the clean_level to min(10, clean_level + rank).
        '''
        #TODO: write your code here
        try:
            if self.can_clean():
                self.clean_level = min(10, (self.clean_level + self.rank))
        except RoomError:
            print(f'This room cannot be cleaned at the moment.')


    def better_than(self, other: 'Room') -> bool:
        '''
        Returns True if this room is better than the other room.
        If other is not a Room object or a successor of it, raise a TypeError.
        A room is better than another room if it has a higher rank, higher floor and higher clean_level.
        '''
        #TODO: write your code here
        try:
            if other.__class__.__name__ == self.__class__.__name__:
                grade = 0
                grade_other = 0
                if self.rank > other.rank:
                    grade += 1
                elif self.rank < other.rank:
                    grade_other += 1
                if self.clean_level > other.clean_level:
                    grade += 1
                elif self.clean_level < other.clean_level:
                    grade_other += 1
                if self.floor > other.floor:
                    grade += 1
                elif self.floor < other.floor:
                    grade_other += 1
                if grade > grade_other:
                    return True
                else:
                    return False
        except TypeError:
            print(f'Its not possible to compare the rooms.')


    def check_in(self, guests: list[str]):
        '''
        Checks in the guests.
        Raises a RoomError if the room is occupied.
        set the satisfaction to 1.0..
        '''
        #TODO: write your code here
        if len(self.guests) > 0:
            raise RoomError(f'The room is occupied.')
        else:
            for name in guests:
                self.guests.append(name)
            self.satisfaction = 1.0

    def check_out(self):
        '''
        Checks out the guests.
        Raises a RoomError if the room is empty.
        '''
        #TODO: write your code here
        if len(self.guests) < 1:
            raise RoomError
        else:
            self.guests = []

    def move_to(self, other: 'Room'):
        '''
        Moves the guests in this room to the other room.
        Raises a RoomError if the room is empty. (priority 1)
        Raises a RoomError if the other room is occupied. (priority 2)
        A moving includes:
        1. Cheking-in the guests to the other room.
        2. If other is better than this room, the other room's satisfaction is increased by 1.
        3. check-out the guests in this room.
        '''
        #TODO: write your code here
        if len(self.guests) < 1 or len(other.guests) > 0:
            raise RoomError
        other.guests = self.guests
        self.guests.clear()
        if other.better_than(self):
            other.satisfaction += 1.0


#########################################
# Question 2 - do not delete this comment
#########################################

class BudgetRoom(Room):
    ''' Represents a budget room. '''
    def __init__(
        self,
        floor: int,
        number: int,
        clean_level: int,
        rank: int = BASIC_RANK,
        satisfaction: Union[int, float] = 1.0,
        guests: list[str] = [],
        clean_stock = 0):
        ''' Constructor of a budget room object '''
        #TODO: write your code here
        super().__init__(floor, number, clean_level, rank, satisfaction, guests)
        self.clean_stock = clean_stock

    def __repr__(self) -> str:
        ''' Returns a string representation of the room '''
        #TODO: write your code here
        return f'{super().__repr__()}\nclean stock: {self.clean_stock}'

    def can_clean(self) -> bool:
        '''
        Returns True if the room can be cleaned.
        A budget room can be cleaned if its clean_stock is greater than 0.
        '''
        #TODO: write your code here
        if self.clean_stock > 0:
            return True
        else:
            return False
    
    def clean(self):
        '''
        Cleans the room.
        Additionally, the clean_stock is decreased by 1.
        '''
        #TODO: write your code here
        try:
            if self.can_clean():
                self.clean_stock -= 1
        except RoomError:
            print(f'The room cannot be cleaned.')

    def grant_clean(self):
        '''
        Grants a cleaning to the room.
        If the room is empty, raise a RoomError.
        Additionally, increase the satisfaction by 0.5.
        '''
        #TODO: write your code here
        if len(self.guests) < 1:
            raise RoomError
        else:
            self.clean_stock += 1
            self.satisfaction += 0.5

    def grant_snack(self):
        '''
        Grants a snack to the room.
        If the room is empty, raise a RoomError.
        Additionally, increase the satisfaction by 0.8.
        Additionally, decrease the clean_level by 1.
        '''
        #TODO: write your code here
        if len(self.guests) < 1:
            raise RoomError
        else:
            self.satisfaction += 0.8
            self.clean_level -= 1

    def check_in(self, guests: list[str]):
        '''
        Checks in the guests.
        If the room is empty, initialize the clean_stock to 0.
        '''
        #TODO: write your code here
        if not self.guests:
            self.clean_stock = 0
            for name in guests:
                self.guests.append(name)
        else:
            for name in guests:
                self.guests.append(name)

    def move_to(self, other: 'BudgetRoom'):
        '''
        Moves the guests in this room to the other room.
        If the other room is a BudgetRoom, sets its clean_stock to the clean_stock of this room.
        '''
        #TODO: write your code here
        _ = self.guests
        for name in self.guests:
            other.guests.append(name)
        self.check_out()
        if other.__class__.__name__ == self.__class__.__name__:
            other.clean_stock = self.clean_stock


#########################################
# Question 3 - do not delete this comment
#########################################

class LegacyRoom(Room):
    ''' Represents a legacy room. '''

    def __init__(
        self,
        floor: int,
        number: int,
        clean_level: int,
        rank: int = BASIC_RANK,
        satisfaction: Union[int, float] = 2.0,
        guests: list[str] = [],
        minibar_drinks: int = 2,
        minibar_snacks: int = 2):
        ''' Constructor of a legacy room object. '''
        #TODO: write your code here
        super().__init__(floor, number, clean_level, rank, satisfaction, guests)
        self.minibar_drinks = minibar_drinks
        self.minibar_snacks = minibar_snacks
        
    def __repr__(self) -> str:
        ''' Returns a string representation of the room. '''
        #TODO: write your code here
        return f'{super().__repr__()}\nminibar drinks: {self.minibar_drinks}\nminibar snacks: {self.minibar_snacks}'

    def add_drinks(self, quantity: int):
        '''
        Adds drinks to the minibar.
        Increase satisfaction by 0.2 for each drink.
        '''
        #TODO: write your code here
        self.minibar_drinks += quantity
        self.satisfaction += (0.2 * quantity)

    def add_snacks(self, quantity: int):
        '''
        Adds snacks to the minibar.
        Increase satisfaction by 0.3 for each snack.
        '''
        #TODO: write your code here
        self.minibar_snacks += quantity
        self.satisfaction += (0.3 * quantity)

    def check_in(self, guests: list[str]):
        #TODO: write your code here
        super().check_in(guests)
        #self.guests.append(guests)

#########################################
# Question 4 - do not delete this comment
#########################################

class Hotel:
    ''' Represents a hotel. '''

    def __init__(self, name: str, rooms):
        ''' Constructor of a hotel object. '''
        #TODO: write your code here
        self.name = name
        self.rooms = rooms
        #for char in name:
        #    self.name += str(char).lower()

    def __repr__(self) -> str:
        ''' Returns a string representation of the hotel. '''
        #TODO: write your code here
        budget_room = 0
        legacy_room = 0
        other_room = 0
        ocup_room = 0
        for r in self.rooms:
            if len(r.guests) > 0:
                ocup_room += 1
            if type(r) == BudgetRoom:
                budget_room += 1
            elif type(r) == LegacyRoom:
                legacy_room += 1
            else:
                other_room += 1
        return f'{self.name} hotel has:\n{budget_room} BudgetRooms\n{legacy_room} LegacyRooms\n{other_room} other room types\n{self.total_occupied_rooms()} occupied rooms'


    def total_occupied_rooms(self):
        counter = 0
        for r in self.rooms:
            if r.guests:
                counter += 1
        return counter


    def check_in(self, guests: list[str], rank: int) -> Room:
        '''
        Tries to checks in the guests to a room with suitable rank.
        If a room is found, the guests are checked in and the room is returned.
        Otherwise, return None.
        '''
        #TODO: write your code here
        for r in self.rooms:
            if r.rank == rank and len(r.guests) < 1:
                r.check_in(guests)
                return r


    def check_out(self, guest: str) -> Room:
        '''
        Try to check out the guest and all of his roomates.
        If successful, return the room the guest stayed in.
        Otherwise, return None.
        '''
        #TODO: write your code here
        _ = str.lower(guest)
        for r in self.rooms:
            if _ in r.guests:
                r.guests.remove(_)
                return r
        return None


    def upgrade(self, guest: str) -> Room:
        '''
        Try to upgrade the guest and his roommates to a better (Q1) room.
        If successful, return the room the guest stayed in.
        Otherwise, return None.
        '''
        #TODO: write your code here
        _ = str.lower(guest)
        for f_r in self.rooms:
            if _ in f_r.guests:
                cur_room = f_r
                for r in self.rooms:
                    if cur_room.__class__.__name__ == r.__class__.__name__ and len(r.guests) < 1:
                        if r.better_than(cur_room):
                            f_r.move_to(r)
                            return r
        return None


###################################
# Main - do not delete this comment
###################################

def test_hotel():
    rooms = [
        BudgetRoom(15, 140, 5),
        LegacyRoom(12, 101, 6, guests=["Ronen", "Shir"]),
        BudgetRoom(1, 2, 5, guests=["Liat"]),
        Room(2, 23, 6, 3)
        ]
    h = Hotel("Dan",rooms)
    print(h)
    print()
    print(f'upgrade Liat:\n{h.upgrade("Liat")}\n')
    print(h)
    print()
    print(f'check out Ronen:\n{h.check_out("Ronen")}\n')
    print(f'{h}\n')
    print(f'check in Alice and Wonder to a room if rank 2:\n{h.check_in(["Alice", "Wonder"], 2)}\n')
    print(f'check in Alex to a room of rank 3:\n{h.check_in(["Alex"], 3)}\n')
    print(h)
    print()
    print(f'check in Alex to a room of rank 3:\n{h.check_in(["Alex"], 3)}\n')
    print(f'check in Oded and shani to a room of rank 1:\n{h.check_in(["Oded", "Shani"], 1)}\n')
    print(f'check out Liam:\n{h.check_out("Liam")}\n')
    print(f'check out Liat:\n{h.check_out("Liat")}\n')
    print(h)


if __name__ == '__main__':
    test_hotel()
