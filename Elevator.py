class Elevator:

    valid_floors = [1, 2, 3, 4, 5, 6, 7]


    def __init__(self, code):
        self.code = code
        self.current_floor = 1
        self.motor_state = False
        self.doors_state = False
        self.moving = False
        self.floor_path = []
        self.direction = ""

        self.buttons = {
            1 : "Off",
            2 : "Off",
            3 : "Off",
            4 : "Off",
            5 : "Off",
            6 : "Off",
            7 : "Off",
        }


    def __str__(self):
        return "Code: {} - Current Floor: {} - Motor Active: {} - Doors: {} - Moving: {} - Path: {} - Direction: {} - Target Indicator: {}".format(self.code, self.current_floor, self.motor_state, self.doors_state, self.moving, self.floor_path, self.direction, self.buttons)


    def select_floor(self, selection):
        self.buttons[selection] = "On"


    def get_current_floor(self):
        return self.current_floor


    def reset_selection_panel(self):
        for button in self.buttons:
            self.buttons[button] = "Off"
        self.target_indicator = 0


    def request_elevator(self, origin, destiny):
        if origin != self.current_floor:
            print("Elevator: prepairing to pick up")
            self.go_to_floor(origin)
            print("Elevator: arrived to pick up")
            print(self)

        print("Elevator: prepairing for destiny floor")
        self.select_floor(destiny)
        self.go_to_floor(destiny)
        print("Arrived Destiny")
        self.reset_selection_panel()
        self.clear_elevator()
        print(self)


    def go_to_floor(self, destiny_floor):
        if destiny_floor in self.valid_floors and self.current_floor != destiny_floor:
            self.target_indicator = self.buttons[destiny_floor] = "On"
            self.floor_path, self.direction = self.calculate_path(self.current_floor, destiny_floor)
            self.close_doors()
            self.motor_on()
            for f in self.floor_path:
                self.current_floor = f
                print(self)
            self.motor_off()
            self.open_doors()


    def motor_on(self):
        print("Motor - Turning motor on")
        self.motor_state = True
        self.moving = True


    def motor_off(self):
        print("Motor - Turning motor off")
        self.motor_state = False
        self.moving = False


    def open_doors(self):
        print("Doors - Opening doors")
        self.doors_state = "Open"


    def close_doors(self):
        print("Doors - Closing doors")
        self.doors_state = "Closed"


    def is_moving(self):
        return self.moving


    def get_elevator_code(self):
        return self.code


    def clear_elevator(self):
        self.moving = False
        self.floor_path = []
        self.direction = ""


    def calculate_path(self, current, target):
        if current < target:
            path = list(range(current, target + 1, 1))
            self.direction = "Up"
        else:
            path = list(range(current, target - 1, -1))
            self.direction = "Down"
        return path, self.direction
