''' Python Heap Exercise '''

import random
import sys

#########################################
# Question 1 - do not delete this comment
#########################################
class Tank:
    '''
    Represents a single tank.
    '''

    def __init__(self, serial: str):
        '''
        Creates a new tank with a given serial number.
        '''
        #TODO: write your code here
        self._serial = serial.lower()
        self.total_serial = 0

    def serial_number(self) -> int:
        '''
        Returns the serial number of the tank.
        '''
        #TODO: write your code here
        alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
        dict_alpha = {key: value for (key, value) in enumerate(alphabet)}
        self.total_serial = 0
        c = len(self._serial)
        for i in range(len(self._serial)):
            if self._serial[i].isalpha():
                self.total_serial += (dict_alpha.get(self._serial[i]) * (26 ** c))
                c -= 1
        return self.total_serial

    def __eq__(self, other: 'Tank') -> bool:
        '''
        Checks if self equals another tank.
        This is only true when they have the same serial number
        '''
        #TODO: write your code here
        return self._serial == other._serial


    def __gt__(self, other: 'Tank') -> bool:
        '''
        Checks if self is greater than another tank.
        This is only true when self has a larger serial number
        '''
        #TODO: write your code here
        return self.serial_number() > other.serial_number()

    def __lt__(self, other: 'Tank') -> bool:
        '''
        Checks if self is less than another tank.
        This is only true when self has a smaller serial number
        '''
        #TODO: write your code here
        return self.serial_number() < other.serial_number()

    def __repr__(self) -> str:
        '''
        Returns a string in the following format:
        Tank <serial number>
        where <serial number> should be replaced by the serial number of the tank.

        For example for a tank with serial number "ac" the method should return the string
        "Tank ac"
        '''
        #TODO: write your code here
        return f'Tank {self._serial}'

#########################################
# Question 2 - do not delete this comment
#########################################
class Heap:
    '''
    The heap data structure as studied in class.
    Implement it using a list.
    '''

    def __init__(self):
        '''
        Creates a new empty heap.
        fields are heap, size.
        '''
        #TODO: write your code here
        self._heap = []
        self._size = 0

    def __len__(self) -> int:
        '''
        Returns the number of tanks in the heap.
        Should operate in O(1).
        '''
        #TODO: write your code here
        return self._size

    def insert(self, t: Tank):
        '''
        Inserts a given tank into the heap.
        Should run in time O(log(n)).
        '''
        #TODO: write your code here
        self._heap.append(t)
        self._size += 1
        #percolate_up
        child_index = self._size
        parent_index = child_index // 2
        while parent_index != 0 and child_index != 0:
            if self._heap[child_index] > self._heap[parent_index]:
                temp = self._heap[parent_index]
                self._heap[parent_index] = self._heap[child_index]
                self._heap[child_index] = temp
                child_index = parent_index
                parent_index = child_index // 2
            else:
                parent_index = 0


    def find_max(self) -> Tank:
        '''
        Returns the tank with the highest serial number in the heap.
        Does not change the heap.
        Should run in time O(1).
        '''
        #TODO: write your code here
        return self._heap[0]

    def extract_max(self) -> Tank:
        '''
        Returns and removes the tank with the highest serial number in the heap.
        Note that this function will change the heap.
        Should run in time O(log(n)).
        '''
        #TODO: write your code here
        max_num = self._heap[0]
        self._heap[0] = self._heap[len(self._heap)-1]
        self._heap.pop()
        #percolate_down
        i = 0
        parent = self._heap[i]
        left_child = self._heap[2 * i]
        right_child = self._heap[(2 * i) + 1]
        maximal_child = max(left_child, right_child)
        j = self._heap.index(maximal_child)
        while i != 0 and j != 0:
            if parent < self._heap[j]:
                temp = self._heap[j]
                self._heap[j] = self._heap[i]
                self._heap[i] = temp
                i = j
            else:
                i = 0
        return max_num

    def __contains__(self, t : Tank) -> bool:
        '''
        Checks if a given tank is a part of the heap.
        '''
        #TODO: write your code here
        return t in self._heap

    def __repr__(self) -> str:
        '''
        Returns a string representing all the tanks.
        You may decide for yourselves on the format
        '''
        #TODO: write your code here
        n = 1
        for t in self._heap[0: len(self._heap)-2]:
            print(f'{n}-Tank: serial number: {t._serial}')
            n += 1
        return f'{n}-Tank: serial number: {(self._arr[len(self._arr)-1])}'

#########################################
# Question 3 - do not delete this comment
#########################################
class TankEstimator:
    '''
    A class used to estimate the number of produced tanks.
    Keeps all the tanks stored in a heap
    '''

    def __init__(self):
        '''
        Creates a new estimator with an empty heap.
        '''
        #TODO: write your code here
        self.new_heap = Heap()

    def capture_tank(self, t : Tank):
        '''
        Adds the data of a new captured tank and puts it in the heap
        '''
        #TODO: write your code here
        self.new_heap.insert(t)

    def estimate_production(self) -> int:
        '''
        Estimates the total number of produced tanks, based on the information of captured tanks.
        Estimation is done according to the formula presented in the assignment's document.
        '''
        #TODO: write your code here
        k = self.new_heap._size
        m = self.new_heap.find_max().serial_number()
        return m + (m / k)

#########################################
# Question 4 - do not delete this comment
#########################################
def simulation(N: int, k: int, T: int) -> int:
    '''
    Simulates the production of N tanks.
    Returns the approximation of the number of produced tanks.
    '''
    #TODO: write your code here
    sum = 0
    for i in range(T):
        estimator = TankEstimator()
        sample = random.sample(range(N), k)  # creates a sample from the given range of tanks
        for j in sample:
            t = Tank(number_to_string(j))  # converts a number to a tank serial number
            estimator.capture_tank(t)
        sum += estimator.estimate_production()
    print(f"Estimated number of tanks: {int(sum / T)}")

def number_to_string(num):
    '''
    Converts any positive integer to Base26 (letters only) with no 0th case.
    Useful for applications such as spreadsheet columns to determine which
    Letterset goes with a positive integer.
    '''
    if num < 0:
        return ""
    elif num < 26:
        return chr(97 + num)
    else:
        return number_to_string(int((num) / 26)) + chr(97 + (num) % 26)






if __name__ == '__main__':
    N, k, T = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    simulation(N, k, T)