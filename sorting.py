def swap(a,b):
  a,b = b,a
  return a,b


def bubbleSort(aList):
  for passnum in range(len(aList)-1, 0, -1):
    for i in range(passnum):
      if aList[i]>aList[i+1]:
        temp = aList[i]
        aList[i] = aList[i+1]
        aList[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)



def selectionSort(alist):
  for fillslot in range(len(alist)-1, 0, -1):
    positionMax = 0
    for location in range(1, fillslot+1):
      if alist[location] > alist[positionMax]:
        positionMax = location
    temp = alist[fillslot]
    alist[fillslot] = alist[positionMax]
    alist[positionMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


def insertionSort(alist):
  for index in range(1, len(alist)):
    currentValue = alist[index]
    position = index
    while position > 0 and alist[position - 1] > currentValue:
      alist[position] = alist[position -1]
      position = position - 1
    alist[position] = currentValue


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)



