def larger_than(a, b):
  if len(a) > len(b):
    return True
  elif len(b) > len(a):
    return False

  for i in range(len(a)):
    if a[i] == b[i]:
      continue
    elif a[i] > b[i]:
      return True
    else:
      return False
  return False

# print larger_than('112', '111')
# print larger_than('525', '1111')
# print larger_than('11', '0')
# print larger_than('1', '1')

def rooks_are_safe(_input):
  rowCount = 0
  columnCount = 0
  for row in range(len(_input)):
    for column in range(len(_input)):
      if _input[row][column] == 1:
        rowCount += 1
    if rowCount > 1:
      return False

  for column in range(len(_input)):
    for row in range(len(_input)):
      if _input[row][column] == 1:
        columnCount += 1
    if columnCount > 1:
      return False
  return True  

# rooks = [[1,0,0,0],
#          [0,1,0,0],
#          [0,0,0,1],
#          [0,0,0,0]]
# print rooks_are_safe(rooks)

# rooks = [[0,0,0],
#          [1,0,1],
#          [0,0,0]]
# print rooks_are_safe(rooks)      

# rooks = [[1]]
# print rooks_are_safe(rooks)      


def count_negatives(grid):
  numberNegs = 0
  for row in range(len(grid)):
    for column in range(len(grid)):
      if grid[row][column] < 0:
        numberNegs += 1

  return numberNegs

def count_negativesOn(grid):
  numberNegs = 0
  row = 0
  column = 0
  for columns in range(len(grid)):
    if grid[row][columns] < 0:
      numberNegs += 1
    else:
      row += 1

  for rows in range(len(grid) ):
    if grid[column][rows] < 0:
      numberNegs += 1
    else:
      column += 1

  return numberNegs


# l1 = [[-4, -3,-1,1],
#       [-2, -2,1,2],
#       [-1, 1,2,3],
#       [1, 2,4,5]]
# print count_negatives(l1)
# print count_negativesOn(l1)


# l2 = [[-1, 0],
#       [0, 0]]
# print count_negatives(l2)
# print count_negativesOn(l2)


# l3 = [[-2, 0],
#       [-1, 0]]
# print count_negatives(l3)
# print count_negativesOn(l3)


# l4 = [[0]]
# print count_negatives(l4)
# print count_negativesOn(l4)

from itertools import permutations
def pair10(alist):
  pairs = list(permutations(alist, 2))
  pairsDict = {}
  for pair in pairs:
    pairsDict[pair] = sum(pair)

  for key in pairsDict.keys():
    if pairsDict[key] == 10:
      return key

  return "No pair adds to 10"

print pair10([3,4,1,2,9])

print pair10([-11,-20,2,4,30])
print pair10([1,2,9,8])
print pair10([1,1,1,2,3,9])
print pair10([1,1,1,2,3,4,5])