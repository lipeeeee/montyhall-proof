from question import Question
from random import randint
import globals

def main():
    no_change_acc = 0
    change_acc = 0

    # Calculate no change accuracy
    print("Calculating No Change Accuracy...")
    count = 0
    for i in range(globals.EPOCHS):
        veredict = random_attempt(change_door=False)
        if veredict == True:
            count += 1
    no_change_acc = (count / globals.EPOCHS) * 100

    # Calculate change accuracy
    print("Calculating Change Accuracy...")
    count = 0
    for i in range(globals.EPOCHS):
        veredict = random_attempt(change_door=True)
        if veredict == True:
            count += 1
    change_acc = (count / globals.EPOCHS) * 100

    # Print veredict
    print(f"\nChange accuraccy: {(change_acc)}")
    print(f"No Change accuraccy: {(no_change_acc)}")

def random_attempt(change_door):
    question = Question()

    # Choose door
    question.choose(randint(0, 2))

    # Check if change_door
    if change_door == True:
        question.change()

    return question.get_veredict()

def manual_montyhall():
    question = Question()

    # Choose door and print current state
    hidden_door = -1
    choice = int(input("Choose a door(0-2): "))
    question.choose(choice)
    for i in range(len(question.door_map)):
        # Check if door is the chosen one
        if i == choice:
            print(f"Door {i}: Chosen")
        # Check if door is opened
        elif question.opened_map[i] == 1:
            print(f"Door {i}: Goat")
        else:
            hidden_door = i
            print(f"Door {i}: Hidden")

    # Ask change
    change_bool = int(input((f"\nDo you wanna change to the {hidden_door}th door(0-1)? ")))
    if change_bool == 1:
        question.change()

    # Print veredict
    print(f"Got the car: {question.get_veredict()}")

if __name__ == '__main__':
    # only run if compiler started in main.py
    main()