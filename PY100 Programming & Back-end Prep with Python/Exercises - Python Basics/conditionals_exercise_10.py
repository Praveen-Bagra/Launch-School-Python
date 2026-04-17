speed = 0
acceleration = 24
braking_force = 19
is_moving = ( braking_force < acceleration 
              and (speed > 0 or acceleration > 0) )
print(is_moving)

# It will print True

is_moving = ( braking_force < acceleration 
              and speed > 0 or acceleration > 0 )

print(is_moving) # It will still print true. We don't need parantheses 
                 # for current values. 