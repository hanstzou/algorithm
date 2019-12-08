import math
import pprint

p8goal =  [1, 2, 3,
           8, 0, 4,
           7, 6, 5]
p8sample =[1, 2, 3,
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
mapMoves.names = ['left', 'right', 'up', 'down']



# Iterative Deepening DFS

def getChildren(state, transit):
  # transit get all possible transitions
  # (fills None for infeasible transits)
  children = filter(lambda pair: pair[1] != None, enumerate(transit(state)))
  return children


def DLS(state, check_goal, transit, depth):
  if depth == 0:
    return check_goal(state), []
  else:
    children = getChildren(state, transit)
    for pair in children:
      transition, child = pair
      isFound, transitions = DLS(child, check_goal, transit, depth - 1)
      if isFound:
        transitions += [transition]
        return (isFound, transitions)
  return (False, [])


def iterDepthDFS(state, check_goal, transit):
  for depth in range(0, 100):
    isFound, transitions = DLS(state, check_goal, transit, depth)
    if isFound:
      return (isFound, transitions)


# main

def main():
  transit = mapMoves
  names = transit.names
  isFound, transitions = iterDepthDFS(p8sample, lambda s: s == p8goal, transit)
  if isFound:
    print(transitions)
    pprint.pprint(list(map(lambda i: names[i], transitions)))
  pass


if __name__ == '__main__':
  main()

