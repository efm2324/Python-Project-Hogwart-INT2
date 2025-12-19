import sys
from pathlib import Path

# Add the parent directory to sys.path so we can import utils (doesn't work without this)
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.input_utils import ask_choice

houses = {
    "Gryffindor": 0,
    "Slytherin": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0
}

def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
        return houses
    else :
        print("House not found.")
        return False

def display_winning_house(houses):
    max_points = max(houses.values())
    winning_houses = [house for house, points in houses.items() if points == max_points]
    
    if len(winning_houses) > 1:
        print(f"It's a tie! {', '.join(winning_houses)} are tied with {max_points} points!")
    else:
        print(f"The winning house is {winning_houses[0]} with {max_points} points!")

questions = [ 
    ( 
        "You see a friend in danger. What do you do?", 
        ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ), 
    ( 
        "Which trait describes you best?", 
        ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ), 
    ( 
        "When faced with a difficult challenge, you...", 
        ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", 
        "Analyze the problem"], 
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"] 
    ) 
]

def assign_house(character, questions):

    house_scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    attributes = character.get("Attributes", {})

    house_scores["Gryffindor"] += attributes.get("Courage", 0) * 2 

    house_scores["Slytherin"] += attributes.get("Ambition", 0) * 2  

    house_scores["Hufflepuff"] += attributes.get("Loyalty", 0) * 2  

    house_scores["Ravenclaw"] += attributes.get("Intelligence", 0) * 2  

    for question_text, choices, corresponding_houses in questions:
        chosen_value = ask_choice(question_text, choices)
        
        try:
            choice_index = choices.index(chosen_value)
            assigned_house = corresponding_houses[choice_index]
            house_scores[assigned_house] += 3
            
        except ValueError:
            print("Error in processing choice. Skipping this question's points.")
        except IndexError:
            print("Configuration Error: Choices and corresponding houses lists do not match.")

    print("\n--- Summary of Scores ---")
    for house, score in house_scores.items():
        print(f"{house}: {score} points")

    max_score = max(house_scores.values())

    winning_houses = [house for house, score in house_scores.items() if score == max_score]
    
    final_house = winning_houses[0] 
    
    return final_house