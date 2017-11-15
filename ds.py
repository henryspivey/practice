# Lists

# Node Class

class Node:
  def __init__(self, initdata):
    self.data = initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext


# temp = Node(93)
# print (temp.getData())

class UnorderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def add(self, item):
    # adds an element to the beginning of the list
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    return count

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.getData() == item:
        found = True
      else: 
        previous = current
        current = current.getNext()
    if previous == None:
      self.head = current.getNext()
    else: 
      previous.setNext(current.getNext())


  # append method
  # adds to the end of the list
    # end means that next is None
  # our function needs to find the last element and make it's next element the one supplied
  def append(self, item):
    temp = Node(item)
    found = False
    if(self.isEmpty()):
      self.head = temp
    else:
      # traverse the list starting at the head
      current = self.head
      while current.getNext() != None:
        current = current.getNext()
      current.setNext(temp)

mylist = UnorderedList()


mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)

mylist.append(4)

print(mylist.size())






















