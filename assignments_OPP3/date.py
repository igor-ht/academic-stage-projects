class Date:

    def __init__(self,day=1, month=1, year=2022, hours=0, minutes=0):
        if minutes <=59:
            self._minutes = minutes
        else:
            self._minutes = 0
            hours += 1
        if hours <= 24:
            self._hours = hours
        else:
            self._hours = 0
            day += 1
        if day <= 30:
            self._day = day
        else:
            self._day = 0
            month += 1
        if month <= 12:
            self._month = month
        else:
            self._month = 0
            year += 1
        self._year = year

    @property
    def hour(self):
        return self._hours
    @hour.setter
    def hour(self, x):
        if x <= 24 and x >= 0:
            self._hours = x
        else:
            raise ValueError(f'This value is not valid.')

    @property
    def min(self):
        return self._minutes
    @min.setter
    def min(self, x):
        if x <= 59 and x >= 0:
            self._minutes = x
        else:
            raise ValueError(f'This value is not valid.')

    @property
    def days(self):
        return self._day
    @days.setter
    def days(self, x):
        if x <= 24 and x >= 0:
            self._day = x
        else:
            raise ValueError(f'This value is not valid.')

    @property
    def months(self):
        return self._month
    @months.setter
    def months(self, x):
        if x <= 12 and x >= 0:
            self._month = x
        else:
            raise ValueError(f'This value is not valid.')

    @property
    def years(self):
        return self._year
    @years.setter
    def years(self, x):
        self._year = x


    def __str__(self):
        output =  f'{self._day:02d}/{self._month:02d}/{self._year}, {self._hours:02d}:{self._minutes:02d}'
        return output


    def __repr__(self):
        return self.__str__()


    def diff(self, d2):
        total_y = 0
        total_m = 0
        total_day = 0
        total_min = 0
        total_hour = 0


        total_y = d2._year - self._year
        total_m = d2._month - self._month
        total_day = d2._day - self._day
        total_min = d2._minutes - self._minutes
        total_hour = d2._hours - self._hours

        if total_y > 0:
            total_m += (12*total_y)
        if total_m > 0:
            total_day += (30*total_m)
        if total_day > 0:
            total_hour += (24*total_day)

        if total_min == 0 and total_hour == 0:
            return 0

        if total_min < 0:
            total_hour -= total_min // 60
            total_min = total_min % 60
        elif total_min > 59:
            total_hour += total_min // 60
            total_min -= total_min % 60

        if total_hour == 0:
            return total_min
        else:
            return total_hour

    def early_date(self, y, f):
        x = y.diff(f)
        if x <= 0 :
            return True
        else:
            return False

    def eq_dates(self, other):
        if self.same_day(other) == True and self.diff(other) == 0:
            return True
        else:
            return False


    def same_day(self, d2):
        if self._day == d2._day and self._month == d2._month and self._year == d2._year:
            return True
        else:
            return False

