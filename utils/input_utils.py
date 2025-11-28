def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def ask_number(message, min_value=None, max_value=None):
    while True:
        try:    
            courage_lv = int(input(message))
        except ValueError:
            print("enter a valid number.")
            continue 
        while courage_lv < min_value or courage_lv > max_value:
            print(f"Please enter a number between {min_value} and {max_value}.")
            courage_lv = int(input(message))
        return courage_lv

def ask_choice(message, option):
    print(message)
    for i, option in enumerate(option, 1):
        print(f"{i}. {option}")

    choice = ask_number("Your choice: ", 1, len(option))
    return option[choice - 1]

def load_file(file_path):
    try :
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"The file was not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {file_path}: {e}")
    except Exception as e:
        print(f"There was an error loading the file {file_path}: {e}")
    return None
