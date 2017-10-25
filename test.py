import sys, unittest
from io import StringIO
from maze import Maze, execute_code

class my_tests(unittest.TestCase):

    def setUp(self):
        sys.stdout = StringIO()

    def test_maze_start(self):
        maze = Maze(2, "/Users/matteo/Personal/maze-puzzle-test/example1.json", ["Knife", "Potted Plan"])
        maze.start_game()
        maze.reprint_result()
        self.assertIn("Obj. collected", sys.stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
