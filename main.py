from question import Question

def main():
    new_question = Question()

    # Choose door and print current state
    hidden_door = -1
    choice = int(input("Choose a door(0-2): "))
    new_question.choose(choice)
    for i in range(len(new_question.door_map)):
        # Check if door is the chosen one
        if i == choice:
            print(f"Door {i}: Chosen")
        # Check if door is opened
        elif new_question.opened_map[i] == 1:
            print(f"Door {i}: Goat")
        else:
            hidden_door = i
            print(f"Door {i}: Hidden")

    # Ask change
    change_bool = int(input((f"\nDo you wanna change to the {hidden_door}th door(0-1)? ")))
    if change_bool == 1:
        new_question.change()

    # Print veredict
    print(f"Got the car: {new_question.get_veredict()}")

if __name__ == '__main__':
    # only run if compiler started in main.py
    main()