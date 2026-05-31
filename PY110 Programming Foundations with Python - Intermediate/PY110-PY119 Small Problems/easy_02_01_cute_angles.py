# input: float  
# output: string
# rules
#   Explicit:
#       - To return a string representaion of angle in 
#         degrees, minutes and seconds.
#       - To use a degree symbol to represent degrees, a single
#         quote to represent minutes, and a double quote to represent
#         seconds.
#       - There are 60 minutes in a degree, and 60 seconds in a minute.
# Test Cases / Examples
#   print(dms(30) == "30°00'00\"")
#   print(dms(76.73) == "76°43'48\"")
#   print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
#   print(dms(93.034773) == "93°02'05\"")
#   print(dms(0) == "0°00'00\"")
#   print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
# Data Structure and Algorithm:
#   - Initialize degrees = int(angle)
#   - Initialize fractional_part to:
#     angle - int(angle)
#   - Initialize minutes_with_fractional_part to:
#     fractional_part/1 * 60
#   - Initialize minutes to: int(minutes_with_fractiona_part)
#   - Initialize seconds to:
#     int(minutes_with_fractional_part - minutes)/1 * 60
#   - Return the required string

DEGREE = "\u00B0" 

def dms(angle):
    degrees = int(angle)
    fractional_part = angle - int(angle)
    minutes_with_fractional_part = fractional_part/1 * 60
    minutes = int(minutes_with_fractional_part)
    seconds = int((minutes_with_fractional_part - minutes)/1 * 60)

    return (f"{degrees}{DEGREE}{left_adjust_with_0(minutes)}'"
           f'{left_adjust_with_0(seconds)}"')

def left_adjust_with_0(num):
    if len(str(num)) < 2:
        return '0' + str(num)
    
    return str(num)

# All of these examples should print True
print(dms(30)  == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
