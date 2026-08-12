# class Clock:
    # def __init__(self, hours, minutes=0):
        # self._hours = hours
        # self._minutes = minutes
        # self._total_minutes = (hours * 60) + minutes

    # @property
    # def hours(self):
        # return self._hours

    # @property
    # def minutes(self):
        # return self._minutes

    # def __str__(self):
        # return f'{self.hours:02d}:{self.minutes:02d}'
        
    # @classmethod
    # def at(cls, hours, minutes=0):
        # return cls(hours, minutes)

    # def __add__(self, minutes):
        # total_minutes = self._total_minutes + minutes

        # while total_minutes > 1440:
            # total_minutes -= 1440 # Subtracting day's total minutes

        # hours, minutes = divmod(total_minutes, 60)
        # if hours == 24:
            # hours = 0

        # return Clock(hours, minutes)

    # def __sub__(self, minutes):
        # total_minutes = self._total_minutes - minutes

        # while total_minutes < 0:
            # total_minutes += 1440 # Adding day's total minutes

        # hours, minutes = divmod(total_minutes, 60)
        # if hours == 24:
            # hours = 0

        # return Clock(hours, minutes) 

    # def __eq__(self, other_clock):
        # if not isinstance(other_clock, Clock):
            # return NotImplemented

        # return ((self.hours == other_clock.hours) 
                # and (self.minutes == other_clock.minutes))

class Clock:
    ONE_DAY = 24 * 60

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def at(cls, hour, minute=0):
        return cls(hour, minute)

    def __add__(self, add_minutes):
        minutes_since_midnight = self.compute_minutes_since_midnight() + add_minutes
        while minutes_since_midnight >= self.ONE_DAY:
            minutes_since_midnight -= self.ONE_DAY

        return self.compute_time_from(minutes_since_midnight)

    def __sub__(self, sub_minutes):
        minutes_since_midnight = self.compute_minutes_since_midnight() - sub_minutes
        while minutes_since_midnight < 0:
            minutes_since_midnight += self.ONE_DAY

        return self.compute_time_from(minutes_since_midnight)

    def __eq__(self, other_time):
        return self.hour == other_time.hour and self.minute == other_time.minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def compute_minutes_since_midnight(self):
        total_minutes = 60 * self.hour + self.minute
        return total_minutes % self.ONE_DAY

    def compute_time_from(self, minutes_since_midnight):
        hours, minutes = divmod(minutes_since_midnight, 60)
        hours %= 24
        return Clock(hours, minutes)


        

