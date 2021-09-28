class Panel:
    def __init__(self, floor):
        self.floor_panel = floor
        self.button_up = False
        self.button_down = False


    def request_detect(self, request):
        if request == "Up":
            self.button_up = True

        if request == "Down":
            self.button_down = True


    def restore(self):
        self.button_up = False
        self.button_down = False


    def __str__(self):
        return "Panel Floor: {} - Button Up: {} - Button Down {}".format(self.floor_panel, self.button_up, self.button_down)
