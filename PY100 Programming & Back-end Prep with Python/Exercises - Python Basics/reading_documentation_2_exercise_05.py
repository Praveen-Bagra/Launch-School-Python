from datetime import date

today = date.today()

today_year = today.year # Return the year attribute for the date object.
iso_year = today.isocalendar()[0] 
# today.isocalendar() returns a named tuple object with three 
# componenets of date object i.e. ISO year, ISO week and ISO weekday. 
# And we are acessing first element of tuple i.e. ISO year

print(today_year)
print(iso_year)