import random


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
            # attack(self)
            totalOfAttacks += ability.attack()
            # name of variable you assigned in the loop
        return totalOfAttacks


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
        # lowest_attack_value = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        attack_value = random.randint((self.attack_strength // 2), self.attack_strength)
        # Return attack value between 0 and the full attack.
        return attack_value

    def update_attack(self, attack_strength):
        # Update the value of the current attack strength with the # new value passed in as a parameter.
        self.attack_strength = attack_strength


class Weapon(Ability):
    def attack(self):
        # Typo in comments for this function
        """
        This method should return a random value between 0 and the full attack power of the weapon. Hint: The attack power is inherited.
        """
        weapon_attack_value = random.randint(0, self.attack_strength)
        return weapon_attack_value


class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        # self.heroes.remove(name)
        # if Hero in self.hero == ValueError:
        #     return 0
        # Doing something else:
        for i, o in enumerate(self.heroes):
            if Hero == 0:
                return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for h in self.heroes:
            print(hero)


# Testing Code
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print("You have created a hero.".format(hero.name))
    print(hero.attack())
    # Create an ability
    ability = Ability("Divine Speed", 300)
    # Add the ability to the hero
    hero.add_ability(ability)
    # print("You have created an new ability (check properties of a ability).")
    # print("Number of Attacks: {}".format(hero.attack()))
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    # print("You have created another ability.")
    hero.add_ability(new_ability)
    #print("You have added your ability to your hero.")
    print(hero.attack())
    # print("Now that you have added another ability the attack strength should be larger than before.")
    # print("Number of Attacks: {}".format(hero.attack()))
