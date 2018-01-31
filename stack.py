class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def max(self):
    return max(self.items)

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)



# s = Stack()
# print s.isEmpty()

# s.push(4)
# s.push('dog')
# print s.peek()

# s.push(True)
# print s.size()
# print  s.isEmpty()
# s.push(8.4)
# print s.pop()
# print s.pop()
# print s.size()


# m = Stack()
# m.push('x')
# m.push('y')
# m.push('z')
# while not m.isEmpty():
#    m.pop()
#    m.pop()

# def revstring(mystring):
#   if mystring:
#     s = Stack()
#     reversedString = ""
#     for letter in mystring:
#       s.push(letter)
#     for x in range(s.size()):
#       reversedString += s.pop()

#     return reversedString
#   return False

# print revstring('1234567890')


def parChecker(symbolString):
  s = Stack()
  balanced = True
  index = 0
  while index < len(symbolString) and balanced:
    symbol = symbolString[index]
    if symbol == "(":
      s.push(symbol)
    else:
      if s.isEmpty():
        balanced = False
      else:
        s.pop()
    index  = index + 1

  if balanced and s.isEmpty():
    return True
  else:
    return False

print(parChecker('((()))'))
print(parChecker('(()'))


def genericParChecker(symbolString):
  s = Stack()
  balanced = True
  index = 0
  while index < len(symbolString) and balanced:
    symbol  = symbolString[index]
    if symbol in "([{":
      s.push(symbol)
    else:
      if s.isEmpty():
        balanced = False
      else:
        top = s.pop()
        if not matches(top, symbol):
          balanced = False
    index = index + 1
  if balanced and s.isEmpty():
    return True
  else:
    return False


def matches(open, close):
  opens = "([{"
  closers = ")]}"
  return opens.index(open) == closers.index(close)


print(genericParChecker('{{([][])}()}'))
print(genericParChecker('[{()]'))


def divideBy2(decNumber):
  remstack  = Stack()
  while decNumber > 0:
    rem = decNumber % 2
    remstack.push(rem)
    decNumber = decNumber // 2

  binString = ""
  while not remstack.isEmpty():
    binString = binString + str(remstack.pop())

  return binString

print divideBy2(42)



def baseConverter(decNumber, base):
  digits = "0123456789ABCDEF"
  remstack = Stack()
  while  decNumber > 0:
    rem = decNumber % base
    remstack.push(rem)
    decNumber = decNumber // base

  newString = ""
  while not remstack.isEmpty():
    newString = newString+ digits[remstack.pop()]

  return newString


print(baseConverter(25,2))
print(baseConverter(25,8))
print(baseConverter(26,26))
