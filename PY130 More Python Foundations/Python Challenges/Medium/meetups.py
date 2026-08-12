from datetime import date
import calendar

class Meetup:
    WEEKDAYS = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }

    DESCRIPTION = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
        'fifth': 5,
    }

    def __init__(self, year, month):
        self._year = year
        self._month = month

    @property
    def year(self):
        return self._year
        
    @property
    def month(self):
        return self._month

    def day(self, weekday, description):
        description = description.lower()
        weekday_int = Meetup.WEEKDAYS[weekday.capitalize()]

        # first to fifth case
        if description in Meetup.DESCRIPTION:
            return self._first_to_fifth_case(weekday_int, description)

        # last case
        if description == 'last':
            return self._last_case(weekday_int)

        # Teenth Case
        return self._teenth_case(weekday_int)

    def _first_to_fifth_case(self, weekday_int, description):
        _, month_days = calendar.monthrange(self.year, self.month)
        description_int = Meetup.DESCRIPTION[description]

        counter = 0
        for day in range(1, month_days + 1):
            current_date = date(self.year, self.month, day)
            if current_date.weekday() == weekday_int:
                counter += 1
                if counter == description_int:
                    return current_date
        
        return None

    def _last_case(self, weekday_int):
        _, month_days = calendar.monthrange(self.year, self.month)

        for day in range(month_days, 0, -1):
            current_date = date(self.year, self.month, day) 
            if current_date.weekday() == weekday_int:
                return current_date

        return None

    def _teenth_case(self, weekday_int):
        for day in range(13, 20):
            current_date = date(self.year, self.month, day)
            if current_date.weekday() == weekday_int:
                return current_date
