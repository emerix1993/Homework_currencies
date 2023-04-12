
team = [{"name":"bob","age":20,"number":5}]



def menu():
    command1 = input("Enter you choice: ")
    if command1 == "add":
        add_player()
    elif command1 == "del":
        players_del()
    elif command1 == "get":
        get_name_player()
    elif command1 == "list":
        get_all_list()
    elif command1 == "find":
        players_find()

def add_player():
    command_add_name = str(input("Enter player name: "))
    if command_add_name.isdigit():
        print("Error, enter string field")
    command_add_age = int(input("Enter player age: "))
    if command_add_age == str:
        raise TypeError
    command_add_number = None
    while not command_add_number:
        command_add_number = int(input("Enter player number: "))
        if any(player["number"] == command_add_number for player in team):
            print("Player with this number is already in the list, please enter another number: ")
            break
        player = {"name":command_add_name,"age":command_add_age,"number":command_add_number}
        team.append(player)
        print("Player add!")

def get_name_player():
    command_get_name_player = input("Enter player name: ")
    for player in team:
        if command_get_name_player.lower() == player["name"].lower():
            print(player)
        else:
            print("Name Error")
def get_all_list():
    print(team)

def players_find():
    players_find_command = input("Enter players attr: ")
    if players_find_command.isdigit():
        players_find_command = int(players_find_command)
    for player in team:
        if players_find_command == player["name"] or players_find_command == player["age"] or players_find_command == player["number"]:
            print(player)
        else:
            print("Error! This field is not in player list")

def players_del():
    players_del_command = input("Enter name player for delete: ")
    for player in team:
        if players_del_command == player["name"]:
            team.remove(player)
            print("This player delete from list")
        else:
            print("This player not in list")


while True:
    menu()
