
from date import Date
from flight import Flight
from flights import Flights
from trip import Trip

class TravelAgent(Flights):

    def __init__(self, lst):
        self._lst = self.lst_by_date(lst)

    def add_flight(self, f):
        for i in range(len(self._lst) - 1):
            if self._lst[i]._flight_date.early_date(self._lst[i]._flight_date, f._flight_date) == False:
                self._lst.insert(i, f)
        if f not in self._lst:
            self._lst.append(f)

    def all_deals(self, source, destination, date, stop):
        self.all_deal_lst = []
        deals = []
        for f in range(len(self._lst)-1):
            if self._lst[f]._flight_date == date and self._lst[f]._depar == source and self._lst[f]._arr == destination:
                self.all_deal_lst.append(Trip(f))
            elif self._lst[f]._flight_date == date and self._lst[f]._depar == source:
                deals.append(f)
            elif destination == self._lst[f]._arr:
                for i in deals:
                    if i._arr == self._lst[f]._depar:
                        deals.append(f)
                        self.all_deal_lst.append(Trip(deals))
                        deals.clear()
        return self.all_deal_lst





    def remove_flight(self, f):
        if f in self._lst:
            self._lst.remove(f)
        else:
            return f'This flight is not in the list.'

    @property
    def lst_flights(self):
        return self._lst

