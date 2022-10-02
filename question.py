from random import randint

# Main class
class Question:
    def __init__(self):
        self.door_map = {}

        self.map_questions()

    def map_questions(self):
        car_door = randint(0, 2)


        for i in range(3):
            if i == car_door:
                self.door_map[i] = 1
            else:
                self.door_map[i] = 0