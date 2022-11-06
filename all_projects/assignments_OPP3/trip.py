from date import Date
from flight import Flight
from flights import Flights

class Trip(Flights):

    def __init__(self, lst):
        self._lst = self.lst_by_date(lst)

    def get_flight(self, i):
        return self._lst[i]

    def total_duration(self):
        total = 0
        for f in self._lst:
            total += f.duration_flight
        return total

    def total_cost(self):
        total = 0
        for f in self._lst:
            total += f.cost_flight
        return total

    def total_stop(self):
        if len(self._lst) == 1:
            return f'Was a direct flight.'
        elif len(self._lst) > 1:
            return len(self._lst) - 1

    def total_airlines(self):
        if len(self._lst) == 1:
            return self._lst[0]._airline
        else:
            return f'multiple airlines'


    @property
    def flight_lst(self):
        return self._lst
    @flight_lst.setter
    def flight_lst(self, x):
        self._lst = x


    def __str__(self):
        return f'{self._lst[0]._depar} to {self._lst[len(self._lst)-1]._arr}\ndate: {self._lst[0]._flight_date}\nairline: {self.total_airlines()}\ncost: {self.total_cost()}\nduration: {self.total_duration()}\nstops: {self.total_stop()}'


