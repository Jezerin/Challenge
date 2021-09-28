from Elevator import Elevator
from Panel import Panel
from User import User

panels = {
    1 : Panel(1),
    2 : Panel(2),
    3 : Panel(3),
    4 : Panel(4),
    5 : Panel(5),
    6 : Panel(6),
    7 : Panel(7),
}

elevator_1 = Elevator("Elv 1")
elevator_2 = Elevator("Elv 2")

elevators = [
    elevator_1,
    elevator_2
]

user_1 = User("Jhon", 3, 7)
user_2 = User("Jane", 1, 7)
user_3 = User("Sara", 7, 1)
user_4 = User("Mike", 5, 7)

users = [
    user_1,
    user_2,
    user_3,
    user_4
]

for user in users:
    print("----------------------------------------------------------------------------------------------------------------------")
    current_floor = user.get_user_floor()
    destiny_floor = user.get_user_destiny()
    print (user)

    if current_floor < destiny_floor:
        panels[current_floor].request_detect("Up")
    else:
        panels[current_floor].request_detect("Down")

    print (panels[current_floor])

    elevator_1_position = elevator_1.get_current_floor()
    elevator_2_position = elevator_2.get_current_floor()

    floor_difference_1 = abs(elevator_1_position - current_floor)
    floor_difference_2 = abs(elevator_2_position - current_floor)

    if floor_difference_1 < floor_difference_2:
        print ("Choosing elevator {} which is {} floors away".format(elevator_1.get_elevator_code(), floor_difference_1))
        elevator_1.request_elevator(current_floor, destiny_floor)
    elif floor_difference_1 > floor_difference_2:
        print ("Choosing elevator {} which is {} floors away".format(elevator_2.get_elevator_code(), floor_difference_2))
        elevator_2.request_elevator(current_floor, destiny_floor)
    else:
        print ("Both elevators are on the same floor, arbitrarily choosing elevator 1")
        elevator_1.request_elevator(current_floor, destiny_floor)

    user.update_floor(destiny_floor)
    panels[current_floor].restore()

    print (panels[current_floor])
    print (user)
