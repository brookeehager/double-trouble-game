import random, sys, time

# ----------------------------------------Classes------------------------------- #
class Character:
    def __init__(self, name, age, energy, power, focus):
        self.name = name
        self.age = age
        self.energy = energy
        self.power = power
        self.focus = focus

pta_mom = Character("Karen", 35, 70, 10, 8)
hippy_mom = Character("Leslie", 30, 80, 8, 10)
basic_mom = Character("Ashley", 25, 100, 7, 8)

# Troublemakers (the twins)
class Twin:
    def __init__(self, name, power, energy):
        self.name = name
        self.power = power
        self.energy = energy

twin1 = Twin("Evelyn", 5, 25)
twin2 = Twin("Logan", 5, 25)

# ----------------------------------------------Functions----------------------------------------#
def twin_select(twin1, twin2):
    twinList = [twin1, twin2]
    twin_chance = random.randint(0,1)
    opponent = twinList[twin_chance]
    return opponent

def power_ups():
    power_ups = ["a cup of coffee", "a protein bar", "time for a nap"]
    power_up_chance = random.randint(0,2)
    power_up_drop = power_ups[power_up_chance]
    return power_up_drop

def scenario():
    scenario = ["made a mess", "drawn on the wall", "gotten into your makeup", "gotten peanut butter all over the dog"]
    scenario_chance = random.randint(0,3)
    scenario_choice = scenario[scenario_chance]
    return scenario_choice

def game_end(character):
    if character.energy < 1:
        print("Oh no, you're exhausted!")
        print("It looks like the twins have worn you out this time.")
        sys.exit()

# ----------------------------Introduction----------------------- #
def intro():        # Silly little title page
    print("|------------------------------|")
    print("|                              |")
    print("|        Double Trouble        |")
    print("|       by Brooke Hager        |")
    print("|                              |")
    print("|------------------------------|")
    time.sleep(0.5)
    # -----------Game Explanation------------- #
    print("\n\n* You are the mom of Evelyn and Logan, three year old twins.")
    time.sleep(1)
    print("* The goal of the game is to make it to bedtime.")
    time.sleep(1)
    print("* You will face many challenges and obstacles along the way,")
    print("  Evelyn and Logan will not go down without a fight.")
    time.sleep(1)
    print("* With the right amounts of energy and focus, you can make it to bedtime victorious!")
    time.sleep(1)