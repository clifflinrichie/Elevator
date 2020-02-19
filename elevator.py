# Elevator Program using two queues
# 2/19/2020

from queue import Queue 

# each floor's occupation
arrFloor = [0, 0, 0, 0, 0, 0]

# elevator queue
e1 = Queue(maxsize = 0)
# where the elevator currently resides
e1_index = 0

def travel_to_floor(f) :
    global e1_index
    global arrFloor
    # subtract by one since index of first floor is 1
    f = int(f) - 1

    while e1_index != f :
        # add 1 to make it understandable
        print("Passing through floor: ", e1_index + 1)
        e1_index += 1

    # change the occupation, show that one elevator currently resides at 5th floor
    arrFloor[e1_index] = arrFloor[e1_index] + 1
    print("Arrived at floor ", e1_index + 1)
    
    

request = input("Enter elevator floor: ")
travel_to_floor(request)
print("Floor occupation", arrFloor)


