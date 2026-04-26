# input: length and width of a room in meters. It will be strings.
# output: Will print the room's area in square meters and square feet
# Test Cases:
#   Length = 23m, Width = 56m. Prints 1288 sq meters or 13863.9032 sq 
#   feets.
#   Length = 0m, widht = 2m. Prints 0 sq meteres or 0 sq feets.
# Data Structure and Algorith
#   i. Ask user for length and breadth in meteres. Convert them to floats.
#   ii. Calculate area in sq meters and sq feets.
#       a. area in sq meters = length in meters * width in meters
#       b. area in sq feet = area in sq meteres * 10.7639
#   iii. Print the room's area.

room_length_in_meters = float(input("Please enter room's length in meters: "))
room_width_in_meters = float(input("Please enter room's width in meters: "))
area_sq_meters = room_length_in_meters * room_width_in_meters
areq_sq_feets = area_sq_meters * 10.7639

print()
print( f"Room's area is {area_sq_meters:.2f} square meters "
       f"or {areq_sq_feets:.2f} square feet." )

# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room is {area_in_meters:.2f} "
      # f"square meters ({area_in_feet:.2f} square feet).")