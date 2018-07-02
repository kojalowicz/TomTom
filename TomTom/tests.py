import unittest
import main


class MyTest(unittest.TestCase):

    # Good Game
    text_good_map = main.checking_file("maps\map_good.txt")
    good_game = main.Map(text_good_map)
    good_map = good_game.mapping()
    good_move = main.Moves(good_game.list_of_rooms)
    current_room = good_game.list_of_rooms[0].name

    # Map with wrong direction
    text_wrong_direction = main.checking_file("maps\map_wrong_direction.txt")
    wrong_direction_game = main.Map(text_wrong_direction)
    wrong_direction_game.mapping()

    # Map with wrong room
    text_wrong_room = main.checking_file("maps\map_wrong_room.txt")
    wrong_room_game = main.Map(text_wrong_room)
    wrong_room_game.mapping()
#
    # Map with undefined direction
    text_undefined_direction = main.checking_file("maps\map_undefined_direction.txt")
    undefined_direction_game = main.Map(text_undefined_direction)
    undefined_direction_game.mapping()

    # Map with repeated rooms
    text_repeated_rooms = main.checking_file("maps\map_repeated_rooms.txt")
    repeated_rooms_game = main.Map(text_repeated_rooms)
    repeated_rooms_game.mapping()

    # Map with some gibberish
    text_some_gibberish = main.checking_file("maps\map_some_gibberish.txt")
    some_gibberish_game = main.Map(text_some_gibberish)
    some_gibberish_game.mapping()

    def test1_good_room_and_good_move_n(self):
        self.assertEqual(self.good_move.move("n", self.good_game.list_of_rooms[0].name), "r3")

    def test2_good_room_and_good_move_s(self):
        self.assertEqual(self.good_move.move("s", self.good_game.list_of_rooms[1].name), "r3")

    def test3_good_room_and_good_move_e(self):
        self.assertEqual(self.good_move.move("e", self.good_game.list_of_rooms[4].name), "r3")

    def test4_good_room_and_good_move_w(self):
        self.assertEqual(self.good_move.move("w", self.good_game.list_of_rooms[3].name), "r4")

    def test5_good_room_and_wrong_move(self):
        self.assertEqual(self.good_move.move("s", self.good_game.list_of_rooms[0].name), self.good_game.list_of_rooms[0].name)

    def test6_wrong_room_and_good_move(self):
        self.assertEqual(self.good_move.move("s", "nsns"), None)

    def test7_wrong_room_and_wrong_move(self):
        self.assertEqual(self.good_move.move("t", "nsns"), None)

    def test8_map_test_good_map(self):
        self.assertEqual(self.good_map, self.good_map) # Purposeful action because we know that a good map does not return False

    def test9_map_test_wrong_direction(self):
        self.assertEqual(self.wrong_direction_game.mapping(), False)

    def test10_map_test_wrong_room(self):
        self.assertEqual(self.wrong_room_game.mapping(), False)

    def test11_map_test_undefined_direction(self):
        self.assertEqual(self.undefined_direction_game.mapping(), False)

    def test12_map_test_undefined_direction(self):
        self.assertEqual(self.repeated_rooms_game.mapping(), False)

    def test13_map_test_some_gibberish(self):
        self.assertEqual(self.some_gibberish_game.mapping(), False)

    def test14_test_main_with_bed_map(self):
        self.assertEqual(main.main_bad_map(), None)

    def test15_test_main_automated_with_good_map(self):
        self.assertEqual(main.main_automated(["n", "n", "e", "s", "e", "e", "s", "x"]), None)


if __name__ == '__main__':
    unittest.main()
