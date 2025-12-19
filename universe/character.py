#import difflib
from utils.input_utils import load_file


def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }
    return character

def display_character(character):
    print("Character profile:")
    print(f"Last name: {character.get('Last Name')}")
    print(f"First name: {character.get('First Name')}")
    print(f"Money: {character.get('Money', 0)}")
    print("Inventory:")
    print("Spells:")
    print("Attributes:")
    attributes_dict = character.get("Attributes", {})
    attribute_keys = ["Courage", "Intelligence", "Loyalty", "Ambition"]
    for attr in attribute_keys:
        value = attributes_dict.get(attr)
        if value is not None:
            print(f"- {attr}: {value}")
        
def modify_money(character, amount):
    character["Money"] += amount
    return character["Money"]
    
def add_item(character, key, item):
    # avoid duplicates
    if item in character["Inventory"] or item in character["Spells"]:
        return False
    
    if key == "Inventory":
        character["Inventory"].append(item)
        return True
    elif key == "Spells":
        character["Spells"].append(item)
        return True
    
    return "Item not found. Check spelling."