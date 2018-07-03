class Room:
    def __init__(self, name_=""):
        self.name = name_
        self.possible_directions = {}
        self.position_x = None
        self.position_y = None

    def __str__(self):
        return self.name


class Map:
    def __init__(self, text_map):
        self.text_map = text_map
        self.list_of_rooms = []
        self.moves = {"n": [0, 1], "s": [0, -1], "w": [-1, 0], "e": [1, 0]}


    def creating_list_elements(self, text_map=None):
        set_list_of_rooms = False
        if text_map is None:
            text_map = self.text_map
            set_list_of_rooms = True
        list_of_rooms = []
        lines = text_map.split("\n")
        for line in lines:
            room_info = line.split(" ")
            room = Room(room_info[0])
            i = 1
            while i < len(room_info):
                direction = room_info[i].split(":")
                if direction[0] in self.moves.keys():
                    room.possible_directions[direction[0]] = direction[1]
                else:
                    print("Error in map: \n directions name: " + str(direction[0]))
                    return False
                i += 1
            list_of_rooms.append(room)
        if set_list_of_rooms is True:
            self.list_of_rooms = list_of_rooms
        return list_of_rooms

    def rooms_positions(self, list_of_rooms=None, moves=None):
        if self.creating_list_elements() is False:
            return False
        set_popositions = False
        if list_of_rooms is None:
            list_of_rooms = self.list_of_rooms
            set_popositions = True
        if moves is None:
            moves = self.moves
        # calculation of the position of room 0
        list_of_rooms[0].position_y = 0
        list_of_rooms[0].position_x = 0
        # The assumption is simple if the position is empty then count, if it is counted, check the coordinates
        for i in range(len(list_of_rooms)):
            for room in list_of_rooms:
                if room.position_y is not None:
                    for direction in room.possible_directions.keys():
                        if direction in moves.keys():
                            for room_to_move in list_of_rooms:
                                if room_to_move.name == room.possible_directions[direction]:
                                    if room_to_move.position_y is None:
                                        room_to_move.position_x = room.position_x + moves[direction][0]
                                        room_to_move.position_y = room.position_y + moves[direction][1]
                                    elif room_to_move.position_x != room.position_x + moves[direction][0]\
                                            or room_to_move.position_y != room.position_y + moves[direction][1]:
                                        print("Error in map: \n" +
                                            "From: " + room.name + " To: " + room_to_move.name + " direction: " + direction)
                                        return False

        if set_popositions is True:
            self.list_of_rooms = list_of_rooms
        return list_of_rooms

    def repeated_name(self, list_of_rooms=None):
        if list_of_rooms is None:
            list_of_rooms = self.list_of_rooms
        names = []
        for room in list_of_rooms:
            if room.name not in names:
                names.append(room.name)
            else:
                print("Error in map: \n repeated name: " + str(room.name))
                return False
        return names

    def possible_room_to_move(self, list_of_rooms=None):
        if list_of_rooms is None:
            list_of_rooms = self.list_of_rooms
        moves = []
        for room in list_of_rooms:
            for move in room.possible_directions.values():
                if move not in moves:
                    moves.append(move)
        for room in list_of_rooms:
            if room.name not in moves:
                print("Error in map: \n no name: " + str(room.name) + " in possible directions.")
                return False
        return moves

    def print_position(self, text_map):
        if self.mapping() is False:
            print("Error in map:")
            self.mapping()
        else:
            for room in self.list_of_rooms:
                position = "X: " + str(room.position_x) + " Y: " + str(room.position_y)
                print("\n" + room.name + ":")
                print(position)

    def mapping(self):
        list_elements = self.creating_list_elements()
        locations = self.rooms_positions()
        names = self.repeated_name()
        moves = self.possible_room_to_move()
        if list_elements is not False:
            if locations is not False:
                if names is not False:
                    if moves is not False:
                        return self.list_of_rooms

        print("Error in map: \n check the map.")
        return False


class Moves:
    def __init__(self, map):
        self.map = map
        self.possible_moves = {}

    def possible_moves_in_room(self, current_room=str):
        if self.map is not False:
            for room in self.map:
                if room.name == current_room:
                    return room.possible_directions
        else:
            print("Error in map - check the map")
            return None

    def move(self, next_move=str, current_room=str):
        name_rooms = []
        for room in self.map:
            self.possible_moves[room.name] = room.possible_directions
            name_rooms.append(room.name)
        try:
            if current_room in name_rooms:
                if next_move in self.possible_moves[current_room].keys():
                    return self.possible_moves[current_room][next_move]
                else:
                    print("There is no possible directions in this room")
                    return current_room
            else:
                print("There is '" + current_room + "' no room on the list")
        except ValueError:
            return "Something went wrong during the moving"

