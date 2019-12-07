import unittest
import iddfs

class Test8Puzzle(unittest.TestCase):
  topLeft      = [0 if i == 0 else 1 for i in range(9)]
  topMiddle    = [0 if i == 1 else 1 for i in range(9)]
  topRight     = [0 if i == 2 else 1 for i in range(9)]
  leftMiddle   = [0 if i == 3 else 1 for i in range(9)]
  center       = [0 if i == 4 else 1 for i in range(9)]
  rightMiddle  = [0 if i == 5 else 1 for i in range(9)]
  bottomLeft   = [0 if i == 6 else 1 for i in range(9)]
  bottomMiddle = [0 if i == 7 else 1 for i in range(9)]
  bottomRight  = [0 if i == 8 else 1 for i in range(9)]

  # sample goals:
  #   s312
  #     - start from s312
  #     - move 0 to 1. down, 2. right, 3. up
  #     - success (equals to goal)
  directions = ['left', 'right', 'up', 'down']
  goal = [1, 2, 3,
          8, 0, 4,
          7, 6, 5]
  s0    = [1, 2, 3,
           8, 4, 0,
           7, 6, 5]
  s3    = [1, 0, 3,
           8, 2, 4,
           7, 6, 5]
  s21   = [1, 2, 3,
           7, 8, 4,
           0, 6, 5]
  s312  = [1, 2, 3,
           0, 6, 4,
           8, 7, 5]

  def testCountMoves(self):
    fp = iddfs.countMoves
    self.assertEqual(fp(self.topLeft), 2)
    self.assertEqual(fp(self.topRight), 2)
    self.assertEqual(fp(self.bottomLeft), 2)
    self.assertEqual(fp(self.bottomRight), 2)
    self.assertEqual(fp(self.topMiddle), 3)
    self.assertEqual(fp(self.leftMiddle), 3)
    self.assertEqual(fp(self.rightMiddle), 3)
    self.assertEqual(fp(self.bottomMiddle), 3)
    self.assertEqual(fp(self.center), 4)

  def testMoveUp(self):
    fp = iddfs.moveUp
    self.assertEqual(fp(self.topLeft), None)
    self.assertEqual(fp(self.leftMiddle), self.topLeft)
    self.assertEqual(fp(self.center), self.topMiddle)
    self.assertEqual(fp(self.rightMiddle), self.topRight)
    self.assertEqual(fp(self.bottomRight), self.rightMiddle)

  def testMoveRight(self):
    fp = iddfs.moveRight
    self.assertEqual(fp(self.topRight), None)
    self.assertEqual(fp(self.rightMiddle), None)
    self.assertEqual(fp(self.leftMiddle), self.center)
    self.assertEqual(fp(self.center), self.rightMiddle)
    self.assertEqual(fp(self.bottomLeft), self.bottomMiddle)

  def testMoveLeft(self):
    fp = iddfs.moveLeft
    self.assertEqual(fp(self.bottomLeft), None)

  def testMapMoves(self):
    fp = iddfs.mapMoves # left, right, up, down
    self.assertEqual(list(fp(self.topRight)),
        [self.topMiddle, None, None, self.rightMiddle])

  def testDFS(self):
    fp = iddfs.DFS
    self.assertEqual(fp(self.goal, self.goal, 0), (True, []))
    self.assertEqual(fp(self.s0,   self.goal, 0), (False, []))
    self.assertEqual(fp(self.s0,   self.goal, 1), (True, [0]))
    self.assertEqual(fp(self.s3,   self.goal, 1), (True, [3]))
    self.assertEqual(fp(self.s21,  self.goal, 2), (True, [2, 1][::-1]))
    self.assertEqual(fp(self.s312, self.goal, 3), (True, [3, 1, 2][::-1]))

  def testIDDFS(self):
    fp = iddfs.iterDepthDFS
    self.assertEqual(fp(self.goal, self.goal), (True, []))
    self.assertEqual(fp(self.s0,   self.goal), (True, [0]))
    self.assertEqual(fp(self.s3,   self.goal), (True, [3]))
    self.assertEqual(fp(self.s21,  self.goal), (True, [2, 1][::-1]))
    self.assertEqual(fp(self.s312, self.goal), (True, [3, 1, 2][::-1]))
    goal = [1, 2, 3, 4,
           12,13,14, 5,
           11, 0,15, 6,
           10, 9, 8, 7 ]
    sample = [1, 2, 4, 5,
             12,14, 0, 6,
             11, 9, 3,15,
             10, 8,13, 7 ]
    moves = [3, 0, 3, 0, 2, 2, 1, 1, 2, 0, 3, 3]
    self.assertEqual(fp(sample, goal), (True, moves))

def main():
  unittest.main()

if __name__ == '__main__':
  main()

