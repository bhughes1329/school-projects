# Name: Brooke Hughes
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

def get_user_input():
    '''
    Args:
        none
    Returns:
        (string) user choice for their next course of action
    '''
    return input("Type in your action and press <Enter>: ")

def print_choices(a, b, c):
    '''
    Args:
        a (string): first story option
        b (string): second story option
        c (string): third story option
    Returns:
        nothing
    Prints:
        the three story options in order
        '''
    print(f"a) {a}")
    print(f"b) {b}")
    print(f"c) {c}")


def one_a():
    '''Prints prompt and options when user's first choice is a, and returns user input for decision'''
    print()
    print("He doesn't respond. You then")
    print_choices("Wait patiently in your cell and observe him", "Try to pick the lock on your cell", "Start a small fire")
    return get_user_input()


def two_aa():
    '''Prints prompt and options when user's first choice is a and second choice is a, and returns user input for decision'''
    print()
    print("You notice that the guards switch out every hour. You decide to")
    print_choices("Continue to wait", "Try to convince a new guard to be let out", "Try to pick the lock on your cell during the guard change")
    return get_user_input()


def three_aaa():
    '''Prints result when user's first choice is a, second choice is a, and third choice is a'''
    print()
    print("After hours of waiting, a guard comes in and detains you, saying that it is time for you to be executed.")
    game_over()


def three_aab():
    '''Prints result when user's first choice is a, second choice is a, and third choice is b'''
    print()
    print("The new guard executes you on the spot because you were attempting to escape. Must've had a bad day.")
    game_over()


def three_aac():
    '''Prints result when user's first choice is a, second choie is a, and third choice is c'''
    print()
    print("You are able to pick the lock and escape undetected.")
    you_win()


def two_ab():
    '''Prints prompt and options when user's first choice is a and second choice is b, and returns user input for decision'''
    print()
    print("While you attempt to pick the lock on your cell, the guard questions you. He seems alarmed and nervous.")
    print_choices("Threaten him", "Ask him his name", "Ask to be let out")
    return get_user_input()


def three_abac():
    '''Prints result when user's first choice is a, second choice is b, and third choice is a or c'''
    print()
    print("He panicks and runs off, but almost immediately returns with his supervisor, who definitely isn't as timid. The supervisor kills you on the spot for attempting to escape.")
    game_over()


def three_abb():
    '''Prints result when user's first choice is a, second choice is b, and third choice is b'''
    print()
    print("You ask him his name, and suddenly he starts to tell you his whole life story. After listening to him talk for 45 minutes, he eventually lets you out because he feels bad for talking for that long.")
    you_win()
    

def two_ac():
    '''Prints prompt and options when user's first choice is a, second choice is c, and returns user input for decision'''
    print()
    print("You use a lighter from your pocket to light a small fire in a trash can. You then")
    print_choices("Bang on the door and yell for help", "Wait for a guard to come in", "Hide the fire and wait for it to trigger an alarm")
    return get_user_input()


def three_aca():
    '''Prints result when user's first choice is a, second choice is c, and third choice is a'''
    print()
    print("The guards recognize your attempt to distract them, so they leave you be. In a rage you kick the trash can over, causing the fire to spread. You burn to death.")
    game_over()


def three_acb():
    '''Prints result when user's first choice is a, second choice is c, and third choice is b'''
    print()
    print("After a couple minutes a guard spots the fire and comes in. You are able to knock him out, take his uniform and keys, and escape the facility.")
    you_win()


def three_acc():
    '''Prints result when user's first choice is a, second choice is c, and third choice is c'''
    print()
    print("You notice that all the guards start to evacuate without checking to see where the fire is. You eventually suffocate to death as the smoke from the fire fills the room.")
    game_over()


def one_b():
    '''Prints prompt and options when user's first choice is b, and returns user input for decision'''
    print()
    print("You find a loose tile in the wall and climb into the opening. From there, you make your way into the ventilation system. You then go ")
    print_choices("Left", "Up", "Right")
    return get_user_input()


def two_ba():
    '''Prints result when user's first choice is b and second choice is a'''
    print()
    print("You fall through the vents into the incinerator.")
    game_over()


def two_bb():
    '''Prints prompt and options when user's first choice is b and second choice is b, and returns user input for decision'''
    print()
    print("You come face-to-face with a massive fan. Do you")
    print_choices("Try to go through it", "Try to stick something between the blades", "Use your shoe")
    return get_user_input()


def three_bba():
    '''Prints result when user's first choice is b, second choice is b, and third choice is a'''
    print()
    print("You get sliced up by the blades.")
    game_over()


def three_bbb():
    '''Prints result when user's first choice is b, second choice is b, and third choice is b'''
    print()
    print("You grab a rock and throw it into the fan. It bounces around and eventually hits you square in the head, knocking you out.")
    game_over()


def three_bbc():
    '''Prints result when user's first choice is b, second choice is b, and third choice is c'''
    print()
    print("You try to stick your shoe through the fan blades. Your shoe is destroyed in the process, but the remnants get stuck in the gears and the fan stops. You eventually make your way up to the roof to escape.")
    you_win()


def two_bc():
    '''Prints prompt and options when user's first choice is b and second choice is c, and returns user input for decision'''
    print()
    print("You reach a room with a pile of bones.")
    print_choices("Try to go back into the vent", "Search through the bones", "Try to open the door")
    return get_user_input()


def three_bca():
    '''Prints result when user's first choice is b, second choice is c, and third choice is a'''
    print()
    print("As you scramble up into the vents something drops on the floor. Its a key! You're then able to unlock the door and escape!")
    you_win()


def three_bcb():
    '''Prints result when user's first choice is b, second choice is c, and third choice is b'''
    print()
    print("You begin to search through the bones and suddenly a rat jumps out and bites you. Your vision starts to blur and you pass out.")
    game_over()


def three_bcc():
    '''Prints result when user's first choice is b, second choice is c, and third choice is c'''
    print()
    print("You jiggle the handle, and suddenly alarms start going off. You are found by guards and sentenced to death.")
    game_over()


def one_c():
    '''Prints prompt and options when user's first choice is c,, and returns user input for decision'''
    print()
    print("With incredible acting skills, you pretend to be having a cardiac event")
    print_choices("Try to run out", "Try to fight the guards", "Stay still")
    return get_user_input()


def two_ca():
    '''Prints result when user's first choice is c and second choice is a'''
    print("Admist their confusion, you are able to slip by the guards and out the open cell door. From there you are able to make your way to the entrance and escape.")
    you_win()


def two_cb():
    '''Prints result when user's first choice is c and second choice is b'''
    print()
    print("The guards are surprised at first, but quickly overpower and kill you.")
    game_over()


def two_cc():
    '''Prints result when user's first choice is c and second choice is c'''
    print()
    print("You lay there for a bit while the guards check you out. They soon notice that you're faking it and kill you on the spot.")
    game_over()



def game_over():
    '''Displays a message to the user for when they have lost the game.'''

    print()
    print("GAME OVER.")
    print("Thanks for playing!")


def you_win():
    '''Displays a message to the user for when they have won the game.'''

    print()
    print("YOU WIN!")
    print("Thanks for playing!")



def my_story():
    '''Begins a Choose Your Own Adventure Game using input from the user'''

    # Introduces game to user
    input("Welcome to CHOOSE YOUR OWN ADVENTURE: ESCAPE THE COMPLEX! Press <Enter> to begin!")

    # Starting prompt and choices
    print()
    print("You wake up in a padded room after being captured. After looking around for a way to escape you ")
    print_choices("Try to plead with the guard standing outside", "Feel around the walls for an opening", "Create a distraction")

    # Asks user for their first action to determine next prompt
    user_choice = input("Type in your action and press <Enter>: ")

    # User's first selection is a
    if user_choice == "a":
        user_choice = one_a()

        # User's second selection is a
        if user_choice == "a":
            user_choice = two_aa()

            # User's third selection is a
            if user_choice == "a":
                three_aaa()
            # User's third selection is b
            elif user_choice == "b":
                three_aab()
            # User's third selection is c
            elif user_choice == "c":
                three_aac()


        # User's second selection is b
        elif user_choice == "b":
            user_choice = two_ab()
            
            # User's third selection is a or c
            if user_choice == "a" or user_choice == "c":
                three_abac()
            # User's third selection is b
            elif user_choice == "b":
                three_abb()
            
        # User's second selection is c    
        elif user_choice == "c":
            user_choice = two_ac()
            
            # User's third selection is a
            if user_choice == "a":
                three_aca()
            # User's third selection is b
            elif user_choice == "b":
                three_acb()
            # User's third selection is c
            elif user_choice == "c":
                three_acc()



    # User's first selection is b
    elif user_choice == "b":
        user_choice = one_b()

        # User's second selection is a
        if user_choice == "a":
            user_choice = two_ba()

        # User's second selection is b
        elif user_choice == "b":
            user_choice = two_bb()

            # User's third selection is a
            if user_choice == "a":
                three_bba()
            # User's third selection is b
            elif user_choice == "b":
                three_bbb()
            # User's third selection is c
            elif user_choice == "c":
                three_bbc()

        # User's second selection is c
        elif user_choice == "c":
            user_choice = two_bc()
            
            # User's third selection is a
            if user_choice == "a":
                three_bca()
            # User's third selection is b
            elif user_choice == "b":
                three_bcb()
            # User's third selection is c
            elif user_choice == "c":
                three_bcc()



    # User's first selection is c
    elif user_choice == "c":
        user_choice = one_c()

        # User's second selection is a
        if user_choice == "a":
            user_choice = two_ca()

        # User's second selection is b
        elif user_choice == "b":
            user_choice = two_cb()

        # User's second selection is c
        elif user_choice == "c":
            user_choice = two_cc()