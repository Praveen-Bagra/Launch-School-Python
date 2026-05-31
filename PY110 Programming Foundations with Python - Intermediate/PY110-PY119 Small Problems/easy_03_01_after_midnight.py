# input: integer (minutes)
# output: string (24-hour time format)
# rules:
#   Explicit: 
#       - Returns the time of day in 24-hour format (hh:mm) as string.
#       - If the number is positive, the time is after midnight,
#         if the number is negative, the time is before midnight.
# Test Cases / Examples:
#   print(time_of_day(0) == "00:00")        # True
#   print(time_of_day(-3) == "23:57")       # True
#   print(time_of_day(35) == "00:35")       # True
#   print(time_of_day(-1437) == "00:03")    # True
#   print(time_of_day(3000) == "02:00")     # True
#   print(time_of_day(800) == "13:20")      # True
#   print(time_of_day(-4231) == "01:29")    # True 
# Data Structure and Algorithm:
#   - 

MINUTES_IN_24_HOUR = 1440

def time_of_day(minutes):
    while minutes > 1440 or minutes < 0:
        if minutes > 0:
            minutes -= MINUTES_IN_24_HOUR
        if minutes < 0:
            minutes += MINUTES_IN_24_HOUR
    
    hour_float = minutes / 60
    hour_int = int(hour_float)
    minutes = int(round((hour_float - hour_int) * 60, 0))

    return f'{hour_int:02d}:{minutes:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True