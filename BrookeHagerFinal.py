# Game by Brooke Hager
# Created 3/24/21
# Final version finished 5/10/21
# Midterm for FHSU Programming with Python class
# Description: You're a stay-at-home mom of twin toddlers and you're just trying to make it through the day
# Try to choose the correct paths and make it out alive
# Inspired by my life

# Imports
import logging, time

logging.basicConfig(filename='BrookeHagerFinal_log.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# ---------------------Import classes and functions from functions.py--------------------- #
try:
    from functions import *
    logging.debug("functions.py imported successfully!")
except:
    logging.critical("functions.py not found!")
    print("functions.py file not found!")
    print("Please check the file directory and try again.")

from functions import Character
pta_mom = Character("Karen", 35, 70, 10, 8)
hippy_mom = Character("Leslie", 30, 80, 8, 10)
basic_mom = Character("Ashley", 25, 100, 7, 8)

from functions import Twin
twin1 = Twin("Evelyn", 5, 25)
twin2 = Twin("Logan", 5, 25)

twin_select(twin1, twin2)
power_ups()
scenario()

# -------------------------------------Main battle function---------------------------------------- #
def battle():
    # Calling functions
    time.sleep(2)
    for i in range(3):
        power_up_drop = power_ups()
        opponent = twin_select(twin1, twin2)
        scenario_choice = scenario()
        print("\nOh no!", opponent.name, "has", scenario_choice, "!\n")
        time.sleep(1)
        print("You can...")

        while opponent.energy > 0:              # Choose options
            weapon = input("1. Time out\n2. Take away toys\n3. Ignore\n>>> \n")

            if weapon == "1":
                print("You give", opponent.name, "a time out.")
                time.sleep(1)
                effect = random.randint(0, 10)  # Random choice of whether punishment is effective

                if effect > 2:
                    opponent.energy = opponent.energy - character.power
                    print("You punished", opponent.name, "their energy is now", opponent.energy)
                    time.sleep(1)

                    if opponent.energy > 0:     # Opponent continues fighting
                        character.energy = character.energy - opponent.power
                        print(opponent.name, "resisted, exhausting you.\n")
                        time.sleep(1)
                        print("You now have", character.energy, "energy left.\n")
                        game_end(character)
                        time.sleep(1)

                    else:            # opponent gives up
                        print(opponent.name, "gave in and accepted the consequences.\n")
                        time.sleep(1)
                        print("You find", power_up_drop, "!")
                        character.energy = character.energy + 10
                        print("\nYour energy is now", character.energy)
                        opponent.energy = 25
                        time.sleep(1)
                        break

                else:              # Opponent doesn't take damage but you do
                    print(opponent.name, "is not listening")
                    print(opponent.name, "talks back and exhausts you.")
                    time.sleep(1)
                    character.energy = character.energy - opponent.power
                    print("\nYour energy is now", character.energy)
                    time.sleep(1)

            elif weapon == "2":
                print("You take toys away from", opponent.name)
                time.sleep(1)
                effect = random.randint(0, 10)  # Random choice of whether punishment is effective

                if effect > 2:
                    opponent.energy = opponent.energy - character.focus
                    print("You punished", opponent.name, "their energy is now", opponent.energy)
                    time.sleep(1)

                    if opponent.energy > 0:     # Opponent continues fighting
                        character.energy = character.energy - opponent.power
                        print(opponent.name, "resisted, exhausting you.\n")
                        time.sleep(1)
                        print("\nYou now have", character.energy, "energy left.\n")
                        game_end(character)
                        time.sleep(1)

                    else:         # opponent gives up
                        print(opponent.name, "gave in and accepted the consequences.\n")
                        time.sleep(1)
                        print("You find", power_up_drop, "!")
                        character.energy = character.energy + 10
                        print("\nYour energy is now", character.energy)
                        opponent.energy = 25
                        time.sleep(1)
                        break
                else:              # Opponent doesn't take damage but you do
                    print(opponent.name, "is not listening")
                    time.sleep(1)
                    print(opponent.name, "talks back and exhausts you.\n")
                    time.sleep(1)
                    character.energy = character.energy - opponent.power
                    print("Your energy is now", character.energy, "\n")
                    time.sleep(1)
                    game_end(character)

            elif weapon == "3":
                print("You attempt to ignore", opponent.name)
                ig_chance = random.randint(0,10)

                if ig_chance > 6:          # You don't take damage but win the fight
                    print(opponent.name, "calmed down and solved the problem by themselves")
                    time.sleep(1)
                    break

                else:            # Opponent doesn't take damage but you do
                    print(opponent.name, "got into something else while you were not paying attention.")
                    character.energy = character.energy - opponent.power
                    print("\nYour energy is now", character.energy)
                    time.sleep(1)
                    game_end(character)       # If character energy <0, character dies
            else:
                print("Please choose 1, 2 or 3")
                continue      # Back to beginning

# Boss fight
def boss_fight():
    print("\nIt's almost bedtime...")
    time.sleep(1)
    print("You must ready yourself for battle.")
    time.sleep(1)
    print("\nYou found a venti latte! Your energy is increased by 50.")
    time.sleep(1)
    character.energy = character.energy + 50
    print("Your energy is now", character.energy)
    time.sleep(1.5)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("\nThe time has come to put the twins to bed. Get them both to sleep successfully and you win!")
    time.sleep(1)
    print("However, succumb to exhaustion first and the twins have won.")
    time.sleep(1.5)

    while twin1.energy or twin2.energy <= 0:       # Keep the game going until the twins' energy is gone
        print("\nWhat would you like to do?")
        time.sleep(1)
        print("\n1. Read a storybook\n2. Rock\n3. Tuck in")
        choice = input(">>> ")

        if choice == "1":
            print("You read a storybook to", twin1.name, "and", twin2.name, ".\n")
            time.sleep(1)
            effect = random.randint(0, 10)

            if effect > 5: # Half the time one twin will take damage, half the other twin, depending on the randint
                twin1.energy = twin1.energy - character.power
                print(twin1.name, "is relaxed, their energy is now", twin1.energy)
                if twin1.energy > 0:
                    character.energy = character.energy - twin1.power
                    time.sleep(1)
                    print("\nYou grow tired. Your energy is now", character.energy)   # Character loses energy
                elif twin1.energy <= 0:
                    time.sleep(1)
                    print(twin1.name, "has fallen asleep")
                    time.sleep(1)
                    if twin1.energy and twin2.energy <=0:
                        break       # End loop if twins are out of energy

            elif effect <= 5:
                twin2.energy = twin2.energy - character.power
                print(twin2.name, "is relaxed, their energy is now", twin2.energy)
                time.sleep(1)
                if twin2.energy > 0:
                    character.energy = character.energy - twin2.power
                    print("\nYou grow tired. Your energy is now", character.energy)
                    time.sleep(1)
                elif twin2.energy <= 0:
                    print(twin2.name, "has fallen asleep.")
                    time.sleep(1)
                    if twin1.energy and twin2.energy <= 0:
                        break

        elif choice == "2":
            print("You rock", twin1.name, "and", twin2.name, ".\n")
            time.sleep(1)
            effect = random.randint(0, 10)

            if effect > 5:
                twin1.energy = twin1.energy - character.focus
                print(twin1.name, "is relaxed, their energy is now", twin1.energy)
                time.sleep(1)
                if twin1.energy > 0:
                    character.energy = character.energy - twin1.power
                    print("You grow tired. Your energy is now", character.energy)
                    time.sleep(1)
                elif twin1.energy <= 0:
                    print(twin1.name, "has fallen asleep")
                    time.sleep(1)
                    if twin1.energy and twin2.energy <= 0:
                        break

            elif effect <= 5:
                twin2.energy = twin2.energy - character.focus
                print(twin2.name, "is relaxed, their energy is now", twin2.energy)
                time.sleep(1)
                if twin2.energy > 0:
                    character.energy = character.energy - twin2.power
                    print("You grow tired. Your energy is now", character.energy)
                    time.sleep(1)
                elif twin2.energy <= 0:
                    print(twin2.name, "has fallen asleep.")
                    time.sleep(1)
                    if twin1.energy and twin2.energy <= 0:
                        break

        elif choice == "3":
            print("You tuck", twin1.name, "and", twin2.name, "in.\n")
            time.sleep(1)
            effect = random.randint(0, 10)

            if effect > 5:
                twin1.energy = twin1.energy - character.power
                print(twin1.name, "is relaxed, their energy is now", twin1.energy)
                time.sleep(1)
                if twin1.energy > 0:
                    character.energy = character.energy - twin1.power
                    print("You grow tired. Your energy is now", character.energy)
                    time.sleep(1)
                elif twin1.energy <= 0:
                    print(twin1.name, "has fallen asleep")
                    if twin1.energy and twin2.energy <=0:
                        break

            elif effect <= 5:
                twin2.energy = twin2.energy - character.power
                print(twin2.name, "is relaxed, their energy is now", twin2.energy)
                time.sleep(1)
                if twin2.energy > 0:
                    character.energy = character.energy - twin2.power
                    print("\nYou grow tired. Your energy is now", character.energy)
                    time.sleep(1)
                elif twin2.energy <= 0:
                    print(twin2.name, "has fallen asleep.")
                    if twin1.energy and twin2.energy <=0:
                        break

        else:
            print("Please select 1, 2 or 3.")
            time.sleep(1)
            continue    # Back to beginning of loop if wrong option is selected

    if twin1.energy and twin2.energy <=0:
        print("\nThey have both fallen asleep! You have successfully put both Evelyn and Logan to bed.")
        time.sleep(1)
        print("\nYour remaining energy is now", character.energy)
        time.sleep(1)
        print("Thank you for playing!")
        time.sleep(5)
        sys.exit()

intro()

# ------------------------------------------------Character selection------------------------------------------ #
print("\nWho would you like to play as?")
time.sleep(1)
print("\n1. Karen: the PTA mom who's always organized. Max power but less energy.")
print("\n2. Leslie: the crunchy, hippy mom with organic snacks. Balance of power and energy.")
print("\n3. Ashley: the Instagram mom with a perpetual Starbucks in hand. Less power, max energy.\n")

while True:
    selection = input(">>> ")          # Select which character you want
    if selection == "1":
        character = pta_mom
        print("You have selected ", character.name)
        print("Age: ", character.age)
        print("Energy: ", character.energy)
        print("Power: ", character.power)
        print("Focus: ", character.focus)
        break

    elif selection == "2":
        character = hippy_mom
        print("You have selected ", character.name)
        print("Age: ", character.age)
        print("Energy: ", character.energy)
        print("Power: ", character.power)
        print("Focus: ", character.focus)
        break

    elif selection == "3":
        character = basic_mom
        print("You have selected ", character.name)
        print("Age: ", character.age)
        print("Energy: ", character.energy)
        print("Power: ", character.power)
        print("Focus: ", character.focus)
        break

    else:
        print("Please enter 1, 2, or 3.")
        time.sleep(1)
        continue

battle()
boss_fight()