import random
# === CS 115 Homework 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Brooke Hughes
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 5 ===

class Item:
    """
    Initializes an item with attributes name, damage points, regeneration points, damage type, and whether
    or not the item is consumable
    """
    def __init__(self, name, damage_points, regeneration_points, damage_type, is_consumable):
        self.name = name
        self.damage_points = damage_points
        self.regeneration_points = regeneration_points
        self.damage_type = damage_type
        self.is_consumable = is_consumable

    def __str__(self):
        str = f"Name: {self.name} / Damage Points: {self.damage_points}"
        if self.regeneration_points != 0:
            str += f" / Regeneration Points: {self.regeneration_points}"
        if self.damage_type != None and self.damage_type != "":
            str += f" / Damage Type: {self.damage_type}"
        if self.is_consumable == True:
            str += f" / Consumable"
        return str

    def __lt__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return self.damage_points < other.damage_points

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __repr__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return str(self)

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

class Move:
    """
    Represents an action a character takes in a turn.
    """

    def __init__(self, other_character, item):
        self.other_character = other_character
        self.item = item

    def __str__(self):
        """ pretty prints Move. Do not change, but you can use as an example """
        return "Move: " + "\r\n" + "    Item: " + str(self.item) + "\r\n" + "    Target character: " + str(self.other_character)


class Character:
    def __init__(self, name, max_health_points):
        '''
        Initializes a character with a name, max health points, and a rusty axe item
        '''
        self.name = name
        self.health_points = max_health_points
        self.inventory = {Item("rusty axe", 1, 0, "physical", False):1}

    def __str__(self):
        '''
        Displays a character's name and health points
        '''
        str = f"Name: {self.name} / HP: {self.health_points}"
        return str
    
    def __lt__(self, other):
        '''
        If a character's health points are less than another's, that character object is less than
        the other's.
        '''
        if not isinstance(other, Character):
            return False
        if self.health_points < other.health_points:
            return True
        return False 

    def transfer_loot(self, loot):
        '''
        Transfers all items from loot (dict of Item: quantity) to self.inventory.
        '''
        for item, quantity in loot.items():
            if item in self.inventory:
                self.inventory[item] += quantity
                loot[item] = 0

    def perform_move(self, move):
        '''
        Applies the effects of move to self and move.other_character as long as self.inventory
        contains the item used in the move.
        '''
        if move.item not in self.inventory.keys():
            return
        move.other_character.health_points -= move.item.damage_points
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable == True:
            self.inventory[move.item] -= 1

    def get_next_move(self, other_characters):
        '''
        Returns a Move object targeting the character with the lowest health points using
        the item with the highest damage points from self.inventory.
        '''
        other_character = min(other_characters)
        item = min(self.inventory.keys())
        
        return Move(other_character, item)

class Robot(Character):
    def __init__(self, name, max_health_points):
        '''
        Initializes a robot character, which starts with a shock baton in its inventory
        '''
        super().__init__(name, max_health_points)
        self.inventory[Item("shock baton", 1, 0, "electrical", False)] = 1

    def get_next_move(self, other_characters):
        '''
        Returns a Move object targeting the first character in other_characters using
        the item with the highest damage points from self.inventory.
        '''
        other_character = other_characters[0]
        item = min(self.inventory.keys())
        
        return Move(other_character, item)
    
    def perform_move(self, move):
        '''
        Applies the effects of move to self and move.other_character as long as self.inventory
        contains the item used in the move. If the item's damage type is electrical, deals double damage.
        '''
        if move.item not in self.inventory.keys():
            return
        if move.item.damage_type == "electrical":
            move.other_character.health_points -= move.item.damage_points * 2
        else:
            move.other_character.health_points -= move.item.damage_points
        
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable == True:
            self.inventory[move.item] -= 1

class Zombie(Character):
    def __init__(self, name, max_health_points):
        '''
        Initializes a zombie character, which starts with 3 brain grenades in its inventory
        '''
        super().__init__(name, max_health_points)
        self.inventory[Item("brain grenade", 5, 0, "viral", True)] = 3

    def get_next_move(self, other_characters):
        '''
        Returns a Move object targeting the first character in other_characters using
        the item with the highest damage points from self.inventory.
        '''
        other_character = other_characters[0]
        item = min(self.inventory.keys())
        
        return Move(other_character, item)
    
    def perform_move(self, move):
        '''
        Applies the effects of move to self and move.other_character as long as self.inventory
        contains the item used in the move. If the item's damage type is electrical, deals double damage.
        '''
        if move.item not in self.inventory.keys():
            return
        if move.item.damage_type == "viral":
            move.other_character.health_points -= move.item.damage_points * 2
        else:
            move.other_character.health_points -= move.item.damage_points
        
        self.health_points += move.item.regeneration_points
        if move.item.is_consumable == True:
            self.inventory[move.item] -= 1


class PlayableCharacter(Character):
    def __init__(self, name, max_health_points):
        '''
        Initializes a character that takes in user input to determine the moves it makes
        '''
        super().__init__(name, max_health_points)
        self.inventory[Item("hero's sword", 3, 0, "light", False)] = 1

    def get_user_input(self, other_characters):
        '''
        Prints out user inventory and list of enemies the user can attack
        Asks user for the item they want to use to attack and which enemy they want to attack
        Returns a move object with that item and enemy
        '''
        print("Here is your inventory")
        for item, amt in self.inventory.items():
            print (f"- {item.name} (x{amt})")
        print("")
        print("Here are your enemies:")
        for char in other_characters:
            print(f"{char.name} ({char.health_points} HP)")
        print("")
        print("What is your next move?")
        item_selection = get_inventory_item_from_item_name(input("Enter item name: "), self.inventory)
        target = other_characters[int(input("Enter enemy number: ")) - 1]

        return Move(target, item_selection)
    
    def get_next_move(self, other_characters):
        return self.get_user_input(other_characters)

def spawn_enemies():
    """
    returns enemies based on what has already been implemented

    change this to include any characters you have implemented!
    """
    cubebot_1 = Character("little cubebot", 1)
    cubebot_2 = Character("armor cube", 2)
    return [cubebot_1, cubebot_2]

def standard_battle(main_character, enemies, enemy_that_will_attack):
    """
    Executes one round of combat between the player and a chosen enemy.

    Steps:
    1. The main_character selects a move using get_next_move(enemies).
    2. The main_character applies that move to its chosen target.
    3. If the target's health points reach 0, the main_character transfers
       all items from that target's inventory.
    4. Otherwise, enemy_that_will_attack selects a move using
       get_next_move([main_character]) and applies it.
    5. If the main_character's health points reach 0, the attacking enemy
       transfers all items from the main_character's inventory.
    """
    if main_character.health_points > 0 and enemy_that_will_attack.health_points > 0:
        move = main_character.get_next_move(enemies)
        main_character.perform_move(move)
        if move.other_character.health_points <= 0:
            main_character.transfer_loot(move.other_character.inventory)
        else:
            enemy_move = enemy_that_will_attack.get_next_move([main_character])
            enemy_that_will_attack.perform_move(enemy_move)
            if main_character.health_points <= 0:
                enemy_that_will_attack.transfer_loot(main_character.inventory)

def main_game_loop():
    """
    Do not change. If you would like a different game loop, implement
    one and call it custom_main_game_loop
    """
    main_character = PlayableCharacter("player", 15)
    enemies = spawn_enemies()
    while True:
        print("Main character info: " + str(main_character))
        enemies = [e for e in enemies if e.health_points > 0]
        if not enemies:
            print("You win!")
            break

        enemy = random.choice(enemies)
        standard_battle(main_character, enemies, enemy)
        print(f"Your stats: {main_character}")

        if main_character.health_points <= 0:
            print("You were defeated!")
            break

def get_inventory_item_from_item_name(item_name, inventory):
    """
    Helper function that might make get_next_move for PlayableCharacter easier
    Returns the Item object from inventory (dict with Item keys)
    whose name matches item_name, or None if not found.
    Assumes there will be just one matching item_name in the
    inventory, or will just match the first
    """
    name_matches = filter(lambda item: item.name == item_name, map(lambda i: i, inventory))
    return next(name_matches, None)


if __name__ == "__main__":
    
     # Change any code below to test or run your code
     #other_characters = spawn_enemies()
     #me = PlayableCharacter("alex", 5) #example test code
     #next_move = me.get_next_move(other_characters)
     #print(next_move)
     main_game_loop() # uncomment this to start a game with the staff framework
     #pass