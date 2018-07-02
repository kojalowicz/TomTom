import time
from game import Room, Map, Moves


def checking_file(path):
    file_good = open(path)
    try:
        text = file_good.read()
    finally:
        file_good.close()
    return text


def main():

    text = checking_file("maps\map_good.txt")
    new_game = Map(text)
    new_map = new_game.mapping()
    move = Moves(new_map)
    if new_map is not False:
        current_room = new_map[0].name
        while True:
            print("You are in room: " + current_room)
            if new_game.mapping()is not False:
                print("Possible moves: " + str(move.possible_moves_in_room(current_room).keys()))
                print("For exit press 'x'")
                next_move = input("your choice: ")
                if next_move.strip() == 'x':
                    break
                if next_move in new_game.moves.keys():
                    current_room = move.move(next_move, current_room)
                else:
                    print("Wrong letter, you did not move")
            else:
                print("Error in map - check the map")
                return False


def main_bad_map():

    text = checking_file("maps\map_wrong_direction.txt")
    new_game = Map(text)
    new_map = new_game.mapping()
    move = Moves(new_map)
    if new_map is not False:
        current_room = new_map[0].name
        while True:
            print("You are in room: " + current_room)
            if new_game.mapping()is not False:
                print("Possible moves: " + str(move.possible_moves_in_room(current_room).keys()))
                print("For exit press 'x'")
                next_move = input("your choice: ")
                if next_move.strip() == 'x':
                    break
                if next_move in new_game.moves.keys():
                    current_room = move.move(next_move, current_room)
                else:
                    print("Wrong letter, you did not move")
            else:
                print("Error in map - check the map")
                return False


def main_automated(moves=[]):
    text = checking_file("maps\map_good.txt")
    new_game = Map(text)
    new_map = new_game.mapping()
    move = Moves(new_map)
    if new_map is not False:
        current_room = new_map[0].name
        for move_to in moves:
            print("You are in room: " + current_room)
            if new_game.mapping() is not False:
                print("Possible moves: " + str(move.possible_moves_in_room(current_room).keys()))
                print("For exit press 'x'")
                next_move = move_to
                print("Your choice: " + move_to)
                if next_move.strip() == 'x':
                    break
                if next_move in new_game.moves.keys():
                    current_room = move.move(next_move, current_room)
                else:
                    print("Wrong letter, you did not move")
                time.sleep(1)
            else:
                print("Error in map - check the map")
                return False


if __name__ == "__main__":
    main()
