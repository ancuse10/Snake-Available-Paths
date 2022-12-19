import unittest
from serpiente import numberOfAvailableDifferentPaths

class SnakeTest(unittest.TestCase):
    def test1(self):
        test=1
        snakeMain = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
        board = [4,3]
        depth = 3
        result = 7

        paths = numberOfAvailableDifferentPaths(board,snakeMain,depth)

        self.assertEqual(result,paths,f"Error, result is {result} and you got {paths}")
        results(test,board,snakeMain,depth,paths)
    
    def test2(self):
        test=2
        board = [2, 3]
        snakeMain = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
        depth = 10
        result = 1

        paths = numberOfAvailableDifferentPaths(board,snakeMain,depth)

        self.assertEqual(result,paths,f"Error, result is {result} and you got {paths}")
        results(test,board,snakeMain,depth,paths)

    def test3(self):
        test=3
        board = [10, 10]
        snakeMain = [[5,5], [5,4], [4,4], [4,5]]
        depth = 4
        result = 81

        paths = numberOfAvailableDifferentPaths(board,snakeMain,depth)

        self.assertEqual(result,paths,f"Error, result is {result} and you got {paths}")
        results(test,board,snakeMain,depth,paths)

def results(test,board,snakeMain,depth,paths):
    print("\nTest ",test,"\nBoard: ",board,"\nSnake: ",snakeMain,"\nDepth: ",depth,"\nDifferent paths available: ",paths)

if __name__ == '__main__':
    unittest.main()