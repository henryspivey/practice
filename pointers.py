# Linked Lists

class LinkedNode:
  def __init__(self, value, tail=None):
    self.value = value
    self.next = tail


class LinkedList:
  def __init__(self, *start):
    self.head = None

    for _ in start:
      self.prepend(_)

  def prepend(self, value):
    """add value to front of the list"""
    self.head = LinkedNode(value, self.head)

  def pop(self):
    """remove first value from list"""
    if self.head is None:
      raise Exception("Empty List")
    value = self.head.value
    self.head = self.head.next
    return value

  def __iter__(self):
    n = self.head
    while n is not None:
      yield n.value
      n = n.next

  def remove(self, value):
    n = self.head
    last = None
    while n != None:
      if n.value == value:
        if last is None:
          self.head = self.head.next
        else:
          last.next = n.next
        return True
      last = n
      n = n.next
    return False


a = LinkedList()
a.prepend(1)
a.prepend(2)
a.prepend(3)
a.pop()
a.remove(2)
a.remove(1)
a.remove(1)
for _ in a:
  print (_)



# Detecting Infinite linked list interview question
def checkInfinite(self):
  """Check whether infinite loop via next"""
  p1 = p2 = self
  while p1 != None and p2 != None:
    if p2.next == None: return False

    p1 = p1.next
    p2 = p2.next.next

    if p1 == p2: return True
  return False

















class QueueLinkedList:
  def __init__(self, *start):
    self.head = None
    self.tail = None

    for _ in start:
      self.add(_)

  def append(self, value):
    """add value to end of queue"""
    newNode = LinkedNode(value, None)
    if self.head is None:
      self.head = self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def pop(self):
    """remove first value from list"""
    if self.head is None:
      raise Exception("Empty List")
    value = self.head.value
    self.head = self.head.next
    return value

  def __iter__(self):
    n = self.head
    while n is not None:
      yield n.value
      n = n.next

  def remove(self, value):
    n = self.head
    last = None
    while n != None:
      if n.value == value:
        if last is None:
          self.head = self.head.next
        else:
          last.next = n.next
        return True
      last = n
      n = n.next
    return False

#look into collections.deque


# Trie (prefix tree)
# A prefix tree is a data structure that compactly stores strings

wordkey = '\n'

class PrefixTree:
  def __init__(self):
    self.head = {}

  def add(self, value):
    """add value to prefix tree"""
    d = self.head
    while len(value) > 0:
      c = value[0]
      if c not in d:
        d[c] = {}

      d = d[c]
      value = value[1:]
    if wordkey in d:
      return False
    d[wordkey] = True
    return True

  def __contains__(self, value):
    """determine if value in prefix tree"""
    d = self.head
    while len(value) > 0:
      c= value[0]
      if c not in d:
        return False
      d = d[c]
      value = value[1:]



# stack

def fibonacci(n):
  a = b = 1
  result = [a,b]
  while n >2:
    n =  n -1
    a,b = b, a+b
    result.append(b)
  return result

# print fibonacci(10)
# print fibonacci(100)

# deleting from a list 
# del myList[0] O(n) operation

class Stack:
  # Represented as a list but details kept secret
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    # len is O(1)
    return len(self.stack) ==0

  def push(self, v):
    self.stack.append(v)

  def pop(self):
    if self.isEmpty():
      raise Exception('Stack is Empty')
    return self.stack.pop()

  def __repr__(self):
    return "stack: " + str(self.stack)

s = Stack()
s.push(17)
s.push(19)
print s


# problem : processing time series data
# Circular buffer
class CircularBuffer:
  def __init__(self, size):
    self.size = size
    self.buffer  = [None]*size
    self.low= 0
    self.high = 0
    self.count = 0

  def isEmpty(self):
    return self.count == 0

  def isFull(self):
    return self.count == self.size

  def add(self, value):
    if self.isFull():
      self.low = (self.low+1)%self.size
    else:
      self.count += 1
    self.buffer[self.high] = value
    self.high = (self.high)%self.size

  def remove(self):
    pass

  def __iter__(self):
    idx = self.low
    num = self.count
    while num > 0:
      yield self.buffer[idx]
      idx = (idx+1)%self.size
      num -= 1

  def __repr__(self):
    if self.isEmpty():
      return 'cb:[]'
    return 'cb: [' + ','.join(map(str,self)) + ']'


c = CircularBuffer(4)
print c
c.add(1)
print c
print 1 in c
c.add(7)
c.add(11)
print c.buffer




























