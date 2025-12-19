import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import utils (doesn't work without this)
sys.path.insert(0, str(Path(__file__).parent.parent))

from universe.character import init_character, display_character, modify_money, add_item
from utils.input_utils import load_file, ask_choice, ask_number

def introduction():
    print(".")# Placeholder for introduction text

def create_character():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    attributes = {
        "Courage": int(input("Enter your Courage level (1-10): ")),
        "Intelligence": int(input("Enter your Intelligence level (1-10): ")),
        "Loyalty": int(input("Enter your Loyalty level (1-10): ")),
        "Ambition": int(input("Enter your Ambition level (1-10): "))
    }
    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character

def receive_letter():
    print(
    "An owl flies through the window, delivering a letter sealed with the Hogwarts crest... \n“Dear Student, \nWe are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry!” \nDo you accept this invitation and go to Hogwarts?"
    )# add time for dramatic effect
    answer = int(input("1. Yes, of course! \n2. No, I'd rather stay with Uncle Vernon... ").strip())
    print("Your choice : ", answer)
    if answer == 1:
        print("You have accepted the invitation to Hogwarts!")
    else:
        print("You have declined the invitation to Hogwarts. The adventure ends here.")
        exit(0)

def meet_hagrid():
    print(
    "On your way to Diagon Alley, a giant of man with a wild beard and kind eyes approaches you. \n“Hello there! I'm Hagrid, Keeper of Keys and Grounds at Hogwarts. \nLet me help you get your school supplies!” \n"
    )
    while True:
        try:
            answer = int(input("1. Yes \n2. No ").strip())
        except ValueError:
            print("Invalid input. Please enter the number 1 or 2.")
            continue

        print("Your choice : ", answer)
        if answer == 1:
            print("Hagrid takes you to Diagon Alley, where you buy your wand, books, and robes.")
            break
        elif answer == 2:
            print("Hagrid gently insists and takes you along anyway!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
    
def buy_supplies(character):
    print("Welcome to Diagon Alley!")

    catalog = load_file("data/inventory.json") 

    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"] 

    while required_items:
        print(f"You have {character['Money']} Galleons.")
        print(f"Remaining required items: {', '.join(required_items)}")
        
        choice = ask_number("Enter the number of the item to buy: ")
        
    print("All required items purchased! Choose your pet:")
    pets = ["Owl", "Cat", "Rat", "Toad"]
    pet_prices = {"Owl": 20, "Cat": 15, "Rat": 10, "Toad": 5}
    
    pet_choice = ask_choice("Which pet do you want?", pets)

    display_character(character)