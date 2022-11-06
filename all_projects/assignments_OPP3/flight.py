from date import Date

class Flight:

    def __init__(self, number, flightdate, depar_location, arr_location, duration, cost, seats, airline):
        self._number = number
        self._flight_date = flightdate
        self._depar = depar_location
        self._arr = arr_location
        self._duration = duration
        self._cost = cost
        self._seats = seats
        self._airline = airline
        self._booked = []

    @property
    def get_book_lst(self):
        return self._booked

    @property
    def flight_number(self):
        return self._number
    @flight_number.setter
    def flight_number(self, x):
        self._number = x

    @property
    def flightdate(self):
        return self._flight_date
    @flightdate.setter
    def flightdate(self, x):
        self._flight_date = x

    @property
    def departure_location(self):
        return self._depar
    @departure_location.setter
    def departure_location(self, x):
        self._depar = x

    @property
    def arrival_location(self):
        return self._arr
    @arrival_location.setter
    def arrival_location(self, x):
        self._arr = x

    @property
    def duration_flight(self):
        return self._duration
    @duration_flight.setter
    def duration_flight(self, x):
        self._duration = x

    @property
    def cost_flight(self):
        return self._cost
    @cost_flight.setter
    def cost_flight(self, x):
        self._cost = x

    @property
    def seats_avaiable(self):
        return self._seats
    @seats_avaiable.setter
    def seats_avaiable(self, x):
        self._seats = x

    @property
    def air_line(self):
        return self._airline
    @air_line.setter
    def air_line(self, x):
        self._airline = x

    def __str__(self):
        return f'#{self._number}\n{self._depar} to {self._arr}\ndate: {self._flight_date}\nairline: {self._airline}\ncost: {self._cost}\nseats left: {self._seats}\nduration: {self._duration}'

    def __repr__(self):
        return self.__str__()

    def book_flight(self, name, id):
        if self._seats > 0:
            if (name, id) not in self._booked:
                self._booked.append((name, id))
                self._seats -= 1
            else:
                return f'A reservation in this flight for this name and id has been made already.'
        else:
            return f'The flight number #{self._number} is full'

    def cancel_flight(self, name, id):
        if (name, id) in self._booked:
            self._booked.remove((name, id))
            self._seats += 1
        else:
            return f'No reservation for {name} in flight number #{self._number}'

    def is_booked(self, id):
        for person in self._booked:
            if id in person:
                return True
        return False
