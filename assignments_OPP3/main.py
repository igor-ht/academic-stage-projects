from date import Date
from flight import Flight
from flights import Flights
from trip import Trip
from travel_agent import TravelAgent

d1= Date(3, 4, 2016, 12, 45)
print(d1)
d2= Date(4, 4, 2016, 11, 45)
print(d1.diff(d2))
print(d1.same_day(d2))

print()

d= Date(1, 1, 2016, 8, 45)
f= Flight(895, d, "Tel Aviv", "Rome", 4, 700, 180, "ItalianAir")
print(f)
f.book_flight("Israel Israeli",132938472)
print()
print(f.seats_avaiable)
print(f.is_booked(132938472))

print()

d1= Date(20, 2, 2016, 17, 45)
f1= Flight(895, d1, "Tel Aviv", "Moscow", 4, 250, 200, "Russian Wings")
d2= Date(21, 2, 2016, 2, 45)
f2= Flight(123, d2, "Moscow", "Beijing", 8, 400, 240, "China Air")
flights = []
flights.insert(0, f1)
flights.insert(0, f2)
tr = Trip(flights)
print(tr)