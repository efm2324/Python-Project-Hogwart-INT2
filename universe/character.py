import difflib
from utils.input_utils import load_file


def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": dict(attributes) if attributes is not None else {}
    }
    return character

def display_character(character):
    print("Character Profile:")
    print(f"Last name : {character.get('last_name')}")
    print(f"First name : {character.get('first_name')}")
    print(f"Money : {character.get('money')}")
    print("Attributes :")
    print(f"Spells : {', '.join(character.get('spells', []))}")
    print("Attributes:")
    for attr, value in character.get("Attributes", {}).items():
        print(f" - {attr}: {value}")
        
def modify_money(character, amount):
    character["Money"] += amount
    return character["Money"]
    
def add_item(character, key, item):
    # avoid duplicates
    if item in character["Inventory"] or item in character["Spells"]:
        return False

    catalog = load_file("data/inventory.json")
    if isinstance(catalog, list):
        for entry in catalog:
            if entry.get("name") == item:
                if key.lower() == "spell":
                    character["Spells"].append(item)
                else:
                    character["Inventory"].append(item)
                return True
            
    names = [e.get("name", "") for e in catalog]
    suggestions = difflib.get_close_matches(item, names, n=3, cutoff=0.5)
    if suggestions:
        return f"Item not found. Did you mean: {', '.join(suggestions)}?" # Error 404
    return "Item not found. Check spelling."
