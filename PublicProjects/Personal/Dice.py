# A program I made to further my understanding of classes
# This is also my first attempt at a basic menu and an instance memory

# Allows the user to create theoretical die with an input number of sides
# One or more of a die object can then be "rolled" to produce a random output
# Created die objects and all numbers generated in the instance are stored to lists that function as a "memory" as the instance runs

import random 

class die: 
    def __init__(self, sides): 
        self.sides = sides 

    def roll(self, sides): 
        result = random.randrange(1, sides) 
        return result 

    def roll_mult(self, sides): 
        pass
        values = [] 
        total = 0 
        number = int(input("How many? "))  
        for n in number: 
                results = random.randrange(1, sides) 
                values.append(results) 
        print("Rolls: " + values) 
        for i in values: 
                total += i 
        return values 
    
def toggle_add(): 
    add_results = False 
    if add_results is False: 
        add_results = True 
    else: 
        add_results = False 
        return add_results

def add_die():
    new_die = input("How many sides? ") 
    try: 
        new_die = int(new_die) 
    except: 
        print("Not a valid entry. ")
    return dice_set.append(die(new_die))

def rolling():
    rolls = []
    while True:
        num = 1 
        for die in dice_set: 
            print(f"{num}. d{die.sides}")
            num += 1 
        to_roll = input("Roll which die? Input 0 to view current rolls, the number of the die to roll it, or enter to exit. " )
        if to_roll == "":
            break
        else:
            to_roll = int(to_roll) - 1
        if to_roll == -1:
            print(f"Current rolls: {rolls}") 
            continue
        elif to_roll >= 0 and to_roll < len(dice_set):
            chosen_die = dice_set[to_roll]
            result = chosen_die.roll(chosen_die.sides)
            print(result)
            rolls.append(result) 


run = True 
 
dice_set = [] 

while run is True:
    menu = input("Press 1 to add a new die, press 2 to roll die, press 0 to edit die, or press enter to end. ")
    if menu == "": 
        break 
    elif menu == "1":
        add_die()
    elif menu == "2":
        rolling()

    #multi_roll = input("Roll another? ") 