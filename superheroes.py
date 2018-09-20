import random


class Ability:
    def __init__(self, name, attack_strength):
        #Initialize starting values
        #Set Ability name
        self.name = name
        #Set attack strength
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack values
        # Calculate lowest attack value as an integer.
        lowest_attack_value = 20 // 2
        # Use random.randint(a, b) to select a random attack value.
        attack_value = random.ranint(2, 20)
        # Return attack value between 0 and the full attack.
        return attack_value

    def update_attack(self, attack_strength):
        # Update the value of the current attack strength with the # new value passed in as a parameter.
        self = attack_strength



class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def attack(self):
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attack_strength
        totalOfAttacks = 0
        for ability in self.abilities:
            num = ability.attack_strength
            # attack(self)
            totalOfAttacks += num
            # name of variable you assigned in the loop
            return totalOfAttacks


# Testing Code
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print("You have created a hero.".format(hero.name))
    print("Number of Attacks: {}".format(hero.attack()))
    # Create an ability
    ability = Ability("Divine Speed", 300)
    # Add the ability to the hero
    hero.add_ability(ability)
    print("You have created an new ability (check properties of a ability).")
    print("Number of Attacks: {}".format(hero.attack()))
    new_ability = Ability("Super Human Strength", 800)
    print("You have created another ability.")
    hero.add_ability(new_ability)
    print("You have added your ability to your hero.")
    print("Now that you have added another ability the attack strength should be larger than before.")
    print("Number of Attacks: {}".format(hero.attack()))
