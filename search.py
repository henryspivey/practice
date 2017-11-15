# Binary Search O(log n)

def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False
  count = 0

  while first <= last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
      count += 1
    else:
      if item < alist[midpoint]:
        last = midpoint - 1
      else:
        first = midpoint + 1
      count +=1

  return found, count

testList = [0, 1,2,8, 13, 17, 19,32,42]
print binarySearch(testList, 0)


def recursiveBinarySearch(alist, item):
  if len(alist) == 0:
    return False
  else:
    midpoint = len(alist)//2
    if alist[midpoint] == item:
      return True
    else:
      if item < alist[midpoint]:
        # use the slice operator to 
        recursiveBinarySearch(alist[:midpoint],item)
      else:
        recursiveBinarySearch(alist[midpoint+1:], item)


