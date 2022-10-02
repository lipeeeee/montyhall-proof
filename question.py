from decimal import Overflow
from random import randint

# Main class
class Question:
    def __init__(self):
        self.door_map = {}
        self.opened_map = {} # Map of opened doors(chosen and shown)

        self.map_questions()
        self.map_shown()

    def map_questions(self):
        car_door = randint(0, 2)

        for i in range(3):
            if i == car_door:
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

        # Show a goat
        for i in range(len(self.door_map)):
            if self.door_map[i] != 1 and i != number:
                self.opened_map[i] = 1
                return
