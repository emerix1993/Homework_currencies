team = [{"name":"bob","age":20,"number":5}]


def menu():
    command1 = input("Enter your choice: ")
    match command1:
        case "add":
            add_player()
        case "del":
            players_del()
        case "get":
            get_name_player()
        case "list":
            get_all_list()
        case "find":
            players_find()
        case _:
            print("Invalid command")

def add_player():
    command_add_name = input("Enter player name: ")
    match command_add_name:
        case str(name) if not name.isdigit():
            command_add_age = int(input("Enter player age: "))
            command_add_number = None
            while not command_add_number:
                command_add_number = int(input("Enter player number: "))
                if any(player["number"] == command_add_number for player in team):
                    print("Player with this number is already in the list, please enter another number: ")
                    break
                player = {"name": command_add_name, "age": command_add_age, "number": command_add_number}
                team.append(player)
                print("Player add!")
        case _:
            print("Error! Enter string field.")

def get_name_player():
    command_get_name_player = input("Enter player name: ")
    match command_get_name_player.lower():
        case str(name):
            player_found = False
            for player in team:
                if name == player["name"].lower():
                    print(player)
                    player_found = True
            if not player_found:
                print("Error! Player not found.")
        case _:
            print("Error! Enter string field.")

def get_all_list():
    print(team)

def players_find():
    players_find_command = input("Enter player attribute: ")
    match players_find_command:
        case str(value):
            fields = ["name", "age", "number"]
            player_found = False
            for player in team:
                if value == player["name"] or str(value) == str(player["age"]) or str(value) == str(player["number"]):
                    print(player)
                    player_found = True
            if not player_found:
                print("Error! This field is not in player list")
        case int(value):
            player_found = False
            for player in team:
                if value == player["age"] or value == player["number"]:
                    print(player)
                    player_found = True
            if not player_found:
                print("Error! This field is not in player list")
        case _:
            print("Error! Invalid input.")

def players_del():
    players_del_command = input("Enter name player for delete: ")
    match players_del_command:
        case str(name):
            player_found = False
            for player in team:
                if name == player["name"]:
                    team.remove(player)
                    print("This player has been deleted from the list.")
                    player_found = True
                    break
            if not player_found:
                print("Error! Player not found.")
        case _:
            print("Error! Enter string field.")

while True:
    menu()