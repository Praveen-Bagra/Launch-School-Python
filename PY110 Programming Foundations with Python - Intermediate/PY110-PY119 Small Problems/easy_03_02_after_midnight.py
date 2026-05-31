# input: string (24-Hour Format)
# output: integer
# rules:
#   Explicit:
#       - Write two functions that returns the number of minutes 
#         before and after midnight, respectively.
#       - It should return a value in the range of 0 through 1439.
# Test Cases / Examples
#   print(after_midnight("00:00") == 0)     # True
#   print(before_midnight("00:00") == 0)    # True
#   print(after_midnight("12:34") == 754)   # True
#   print(before_midnight("12:34") == 686)  # True
#   print(after_midnight("24:00") == 0)     # True
#   print(before_midnight("24:00") == 0)    # True
# Data Structure and Algorithm:3
#   - After Midnight
#       - Split the string into two parts seperated by :
#       - initialize variable total_minutes to 
#         (first part * 60) + second part
#       - if total is 1440
#         return 0
#       - Return total_minutes   
#   - Before Midnight
#       - Split the string into two parts seperated by :
#       - initialize variable total_minutes to 
#         1440 - ((first part * 60) + second part)
#       - if total is 1440
#         return 0
#       - Return total_minutes   

def after_midnight(time):
    hours, minutes = time.split(':')
    total_minutes = (int(hours) * 60) + int(minutes)
    if total_minutes == 1440:
        return 0
    return total_minutes
    
def before_midnight(time):
    hours, minutes = time.split(':')
    total_minutes = 1440 - ((int(hours) * 60) + int(minutes))
    if total_minutes == 1440:
        return 0
    return total_minutes

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True