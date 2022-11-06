from date import Date
from flight import Flight

class Flights:
    def __init__(self, lst):
        self._lst = lst

    def lst_by_date(self, lst):
        self.sort_lst = []
        while len(lst) > 0:
            min_date = None
            for i in lst:
                if not min_date:
                    min_date = i
                elif i._flight_date.early_date(min_date._flight_date, i._flight_date) == False:
                    min_date = i
            lst.remove(min_date)
            self.sort_lst.append(min_date)
        return self.sort_lst

    def add_flight(self, f):
        if f not in self._lst:
            self._lst.append(f)

    def get_lst(self):
        return self._lst

    def remove_flight(self, flight):
        if flight in self._lst:
            self._lst.remove(flight)



    def __iter__(self):
        self.n = 0
        return self._lst[self.n]

    def __next__(self):
        x = self.n
        if x == len(self._lst):
            raise StopIteration
        else:
            self.n += 1
            return x



