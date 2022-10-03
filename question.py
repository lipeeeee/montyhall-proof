from random import randint

# Main class
class Question:
    def __init__(self):
        self.chosen_door = None # 0 - 2
        self.car_door = randint(0, 2)
        self.door_map = {}
        self.opened_map = {} # Map of opened doors(chosen and shown)

        self.map_questions()
        self.map_shown()

    def map_questions(self):
        for i in range(3):
            if i == self.car_door:
                self.door_map[i] = 1
            else:
                self.door_map[i] = 0

    def map_shown(self):
        for i in range(3):
            self.opened_map[i] = 0

    def choose(self, number):
        if number > 2 or number < 0:
            Exception("Out of bounds index")
            return -999

        # Update chosen
        self.chosen_door = number

        # Show a goat
        for i in range(len(self.door_map)):
            if self.door_map[i] == 0 and i != self.chosen_door:
                self.opened_map[i] = 1
                return
    
    # Change to the other hidden door
    def change(self):
        for i in range(len(self.door_map)):
            # Choose the door which isnt chosen and it is hidden
            if i != self.chosen_door and self.opened_map[i] == 0:
                self.chosen_door = i
                return

    # returns True or False if the user got the car or not
    def get_veredict(self):
        return self.chosen_door == self.car_door 