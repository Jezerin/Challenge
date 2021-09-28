class User:
    def __init__(self, name, floor, destiny):
        self.name = name
        self.at_floor = floor
        self.destiny_floor = destiny

    def __str__(self):
        return "Name: {} - At Floor: {} - Destiny {}".format(self.name, self.at_floor, self.destiny_floor)


    def get_user_floor(self):
        return self.at_floor


    def get_user_destiny(self):
        return self.destiny_floor


    def update_floor(self, floor):
        self.at_floor = floor
