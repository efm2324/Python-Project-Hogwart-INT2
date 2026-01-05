import random
from utils.input_utils import ask_choice, ask_number, load_file
from universe.house import update_house_points

def create_team(house, team_data, is_player=False, player=None):
    team = {
        "House": house,
        "Score": 0,
        "Seeker": player if is_player else team_data["Seeker"],
        "Chasers": team_data["Chasers"],
        "Beaters": team_data["Beaters"],
        "Keeper": team_data["Keeper"]
    }
    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker=False):

    print(f"\nThe {attacking_team['House']} Chasers are mounting an attack!")
    if random.randint(1, 10) > 5:
        attacking_team["Score"] += 10
        print(f"GOAL! {attacking_team['House']} scores 10 points!")
    else:
        print(f"The {defending_team['House']} Keeper makes a brilliant save!")

def golden_snitch_appears():
    return random.randint(1, 10) == 1

def catch_golden_snitch(team1, team2):

    print("\n THE GOLDEN SNITCH HAS BEEN SPOTTED!")
    print(f"{team1['Seeker']} and {team2['Seeker']} are diving for it!")
    winner = random.choice([team1, team2])
    winner["Score"] += 150
    print(f"Unbelievable! {winner['Seeker']} has caught the Snitch!")
    print(f"150 points to {winner['House']}!")
    return True

def display_score(team1, team2):
    print(f"\nCurrent Score ")
    print(f"{team1['House']}: {team1['Score']}")
    print(f"{team2['House']}: {team2['Score']}")


def quidditch_match(character, houses):
    teams_data = load_file("data/teams_quidditch.json")
    player_house = character["House"]
    opponent_house = "Slytherin" if player_house != "Slytherin" else "Gryffindor"
    
    player_team = create_team(player_house, teams_data[player_house], is_player=True, player=f"{character['First Name']} {character['Last Name']}")
    opponent_team = create_team(opponent_house, teams_data[opponent_house])
    
    print(f"\nWelcome to the match: {player_house} vs {opponent_house}!")
    
    snitch_caught = False
    turn = 0
    
    while not snitch_caught and turn < 20:
        turn += 1
        print(f"\nTurn {turn}")
        attempt_goal(player_team, opponent_team)
        attempt_goal(opponent_team, player_team)
        display_score(player_team, opponent_team)
        
        if golden_snitch_appears():
            snitch_caught = catch_golden_snitch(player_team, opponent_team)

    if player_team["Score"] > opponent_team["Score"]:
        print(f"\nVICTORY FOR {player_house.upper()}!")
        update_house_points(houses, player_house, 50)
    else:
        print(f"\n{opponent_house} wins the match.")
        update_house_points(houses, opponent_house, 50)

def start_chapter_4_quidditch(character, houses):

    print("\nCHAPTER 4: THE QUIDDITCH CUP")
    quidditch_match(character, houses)
    print("\nEnd of Chapter 4!")