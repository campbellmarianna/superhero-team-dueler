import random


class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        # Third parameter for health
        self.armors = list()
        self.start_health = health
        self.health = health
        # self.current_health = current_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    #Add Armor function
    def add_armor(self, armor):
        # Append armor
        self.armors.append(armor)

    def attack(self):
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attack_strength
        totalAttacks = 0
        for ability in self.abilities:
            # attack(self)
            totalAttacks += ability.attack()
            # name of variable you assigned in the loop
        return totalAttacks

    def defend(self):
        """
        This method should calculate the defense attribute from each piece of armor in the hero's list, and add to the total defense.
        NOTE: If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

        # Before anything, check or validate the hero's health
        totalDefense = 0
        # if self.health <= 0:
        #     return totalDefense

        for armor in self.armors:
            totalDefense += armor.defense # <--- this is an attribute/property of Amor class
            # print("Total defense: {}".format(totalDefense))
            # print(type(totalDefense) is int)
        return int(totalDefense) # <------- Should be an Int
        # print("This is the total hero defense: {}".format(totalDefense))

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the hero's health.

        If the hero dies update number of deaths
        """
        # damage amount is an integar
        damage_amt -= self.health
        if self.deaths >= 1:
            self.death += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

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
        # self.num_kills = 0
    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        # print("hero list len: {}".format(len(self.heroes)))
        # Validation check, is the list length zero, if so, you can't iterate
        if len(self.heroes) <= 0:
            # print("self.heroes is empty")
            return 0
        # for every hero object in the list of hero objects...
        for hero in self.heroes:
            # print("HERE")
            # If the current heroes name is equal to the name passed in
            if hero.name == name:
                # print("BEER")
                # remove the hero
                self.heroes.remove(hero)
            else:
                #  for any other cases where the hero isnt found, return a zero
                return 0
        # self.heroes.remove(name)

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if len(self.heroes) <= 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        totalTeamAttackStrengths = 0
        # num_kills = 0
        for hero in self.heroes:
                totalTeamAttackStrengths += hero.attack()
        # return totalTeamAttackStrengths
        num_kills = other_team.defend(totalTeamAttackStrengths)
        for hero in self.heroes:
            if num_kills >= 1:
                hero.add_kill(num_kills)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return the number of heroes that died in attack.
        """
        totalTeamDefense = 0
        excessDamage = 0
        for hero in self.heroes:
            for armor in hero.armors:
                totalTeamDefense += armor.defense

        for hero in self.heroes:
            for ability in hero.abilities:
                damage_amt += hero.ability.attack_strength
        excessDamage = damage_amt - totalTeamDefense
        return self.deal_damage(excessDamage)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heroes that died in attack.
        """
        divisionOfDamage = damage // len(self.heroes)
        numHerosDiedInAttack = 0
        for hero in self.heroes:
            if hero.health > 0:
                hero.health -= divisionOfDamage
                if hero.health <= 0:
                    numHerosDiedInAttack += 1
                    hero.deaths += 1
        return numHerosDiedInAttack

    def revive_heroes(self):
        """
        This method should reset all heroes health to their original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        print(team_name)
        for hero in self.heroes:
            print("{}/s ratio of kills/deaths is {}".format(hero.name, (hero.kills/hero.deaths)))

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            health = 0

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defense)

class Arena(Hero, Team):
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        print("Hi Friend! Welcome to Superheroes!!!")
        print("Make two teams to play!")
        # print("What will name of the first team be?")
        print("To build a team you need and heroes and a team name.")
        print("Later on, you will be able to add cool features to your heroes!")
        print("We'll get into those details later.")

        # Create Hero 1
        name = input("Who will your first hero be?")
        hero1_health = 100
        hero1 = Hero(name, hero1_health)

        self.team_one.add_hero(hero1)
        # self.team_one.team_name = raw_input("What is the name of the first team? ")

        # team_one = Team()
    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics including each heroes kill/death ratio.
        """

# Testing Code - hero and battle test
# if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
#     print("You have created a hero: {}".format(hero.name))
#     # Create an ability
#     ability = Ability("Divine Speed", 300)
#     # Add the ability to the hero
#     hero.add_ability(ability)
#     armor = Armor("Laser Shield", 28)
#     hero.add_armor(armor)
#     print("Defense Value: {}".format(hero.defend()))

# Testing Code - arena test
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()
