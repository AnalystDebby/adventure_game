import time
import random
import string


def enemy():

    enemy_creature = ["'bear', 'dragon', 'bat', 'snake'"
                      ", 'pirate', 'troll', 'wicked fairy'"]
    enemy = random.choice(enemy_creature)
    return enemy


def typewriter_simulator(message):

    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
            time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)

    time.sleep(delay)


def intro(enemy):
    print_pause("You find yourself standing in an open "
                "field, filled with grass and yellow "
                "wild flowers.")
    print_pause(f"Rumor has it that a {enemy()} is"
                " somewhere  around here, and has "
                "been terrifying the nearby village.")
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')

    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def door_choice(weapon, enemy):

    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                "opens and out steps a {enemy()}.")
    print_pause(f"Eep! This is the {enemy()} house!")
    print_pause(f"The {enemy()} attacks you!")
    if 'sword' in weapon:
        victory(weapon, enemy)
    else:

        print_pause("You feel a bit under-prepared for "
                    "this, what with only having a tiny dagger.\n")
    fight(weapon, enemy)


def cave_choice(weapon):

    print_pause('You peer cautiously into the cave.')
    print_pause('It turns out to be only a very small cave.')
    print_pause('Your eye catches a glint of metal behind a rock.')
    print_pause('You have found the magical Sword of Ogoroth!')
    weapon.append('sword')
    print_pause("You discard your silly old dagger and "
                "take the sword with you.")
    print_pause('You walk back out to the field.')
    has_sword(weapon, enemy)


def fight(weapon, enemy):

    fight = numeric_input("Would you like to (1) fight "
                          "or (2) run away?\n", 1, 2)
    if fight == 1:
        print_pause(f"You do your best...but your dagger "
                    "is no  match for the {enemy()}."
                    "You have been defeated!")
        print_pause('GAME OVER!')
        play_or_restart_game()
    elif fight == 2:
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been " "followed.")
        rescue_village(weapon, enemy)


def victory(weapon, enemy):
    cave = numeric_input("Would you like to (1) fight or "
                         "(2) run away?\n", 1, 2)
    if cave == 1:
        print_pause(f"As the {enemy()} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly "
                    "in your hand as you brace yourself "
                    "for the attack.")
        print_pause(f"But the {enemy()} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the "
                    "{enemy()}. You are victorious!")
        play_or_restart_game()
    elif cave == 2:
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been followed")
        rescue_village(weapon, enemy)


def play_or_restart_game():
    choice = string_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'y':  # option 1 (y)
        play_game()
    else:  # option 2 (n)
        print('Thanks for playing! Goodbye!')
        exit(0)


def door_cave_option():

    print_pause('Enter 1 to knock on the door of the house.')
    print_pause('Enter 2 to peer into the cave.')


def here_before():

    print_pause("You've been here before, and gotten "
                "all the good stuff. It's just an empty "
                "cave now.")
    print_pause('You walk back out to the field.')


def has_sword(weapon, enemy):
    door_cave_option()
    has_sword = numeric_input("What would  you like to do? \n"
                              "(Please enter 1 or 2.)\n", 1, 2)

    if has_sword == 1:  # option 1 (y)
        door_choice(weapon, enemy)
    elif has_sword == 2:
        if 'sword' in weapon:
            here_before()
            rescue_village(weapon, enemy)
        else:
            rescue_village(weapon, enemy)


def rescue_village(weapon, enemy):

    door_cave_option()
    choice = numeric_input("What would you like to do? \n"
                           "(Please enter 1 or 2.)\n", 1, 2)

    if choice == 1:
        door_choice(weapon, enemy)
    elif choice == 2:
        cave_choice(weapon)


def string_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Option {option} is invalid. Try again!')


def numeric_input(prompt, minimum, maximum):
    while True:
        option = input(prompt).lower()
        if option.isnumeric():
            option = int(option)
            if minimum <= option <= maximum:
                return option
            else:
                print(f"'Option must be >= {minimum} and"
                      " <= {maximum}!'")
        else:
            print(f'Option {option} must be numeric. Try again!')


def play_game():

    weapon = []
    intro(enemy)
    rescue_village(weapon, enemy)


play_game()


