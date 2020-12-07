import time

max_floors = 10
default_lift = 0
current_human = None
dest_human = None

while 1:
    current_human = int(input("enter current floor: "))
    if current_human > max_floors:
        print(f"Maximum floors are {max_floors}, please enter current floor")
    else:
        break

time.sleep(1)
print("Elevator is coming")
time.sleep(1)
print("Doors opening")
while 1:
    dest_human = int(input("enter destination floor: "))
    if dest_human > max_floors:
        print(f"Maximum floors are {max_floors}, please enter correct destination floor")
    else:
        break
time.sleep(1)
print("Doors closing")
time.sleep(abs(current_human-dest_human))
print("Reached your destination")




