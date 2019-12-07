import math
import pprint

goal =  [1, 2, 3,
         8, 0, 4,
         7, 6, 5]
sample =[1, 2, 3,
         0, 6, 4,
         8, 7, 5]


def countMoves(state):
  possibility = 4
  width = int(math.sqrt(len(state)))
  pos = state.index(0)
  if pos % width in [0, width - 1]:
    possibility -= 1
  if pos < width or pos >= len(state) - width:
    possibility -= 1
  return possibility


def getWidthAndPos(state):
  width = int(math.sqrt(len(state)))
  pos = state.index(0)
  return width, pos


def swapPositions(l, i, j):
  l[i], l[j] = l[j], l[i]
  return l


def moveLeft(state):
  width, pos = getWidthAndPos(state)
  if pos % width == 0:
    return None
  return swapPositions(state.copy(), pos, pos - 1)


def moveRight(state):
  width, pos = getWidthAndPos(state)
  if pos % width == width - 1:
    return None
  return swapPositions(state.copy(), pos, pos + 1)


def moveUp(state):
  width, pos = getWidthAndPos(state)
  if pos < width:
    return None
  return swapPositions(state.copy(), pos, pos - width)


def moveDown(state):
  width, pos = getWidthAndPos(state)
  if pos >= len(state) - width:
    return None
  return swapPositions(state.copy(), pos, pos + width)


def mapMoves(state):
  moveFuncs = [moveLeft, moveRight, moveUp, moveDown]
  return map(lambda fp: fp(state), moveFuncs)


def DFS(state, goal, depth):
  if depth == 0:
    return (state == goal, [])
  else:
    children = filter(lambda pair: pair[1] != None,
                    zip(range(4), mapMoves(state)))
    for pair in children:
      direction, child = pair
      isFound, moves = DFS(child, goal, depth - 1)
      if isFound:
        moves += [direction]
        return (isFound, moves)
  return (False, [])


def iterDepthDFS(state, goal):
  for depth in range(0, 100):
    isFound, moves = DFS(state, goal, depth)
    if isFound:
      return (isFound, moves)


def main():
  directions = ['left', 'right', 'up', 'down']
  isFound, moves = iterDepthDFS(sample, goal)
  if isFound:
    print(moves)
  pass


if __name__ == '__main__':
  main()

