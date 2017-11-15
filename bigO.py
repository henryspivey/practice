# O(n^2)
def min1(numbers):
  currentMin = None
  for x in xrange(len(numbers)):
    currentMin = numbers[x]
    for y in xrange(len(numbers)):
      if(currentMin > numbers[y]):
        currentMin = numbers[y]
  print currentMin

# min1([2,3,-1,0, ])

# O(n)
def min2(numbers2):
  currentMin = numbers2[0]
  for x in xrange(1,len(numbers2)):
    # currentMin = numbers2[x]
    if(currentMin > numbers2[x]):
      currentMin = numbers2[x]
  print currentMin
    
# min2([2,3,-1,0, 100])
