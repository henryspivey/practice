class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)




s=Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


def revstring(mystr):
  # your code here
  s=Stack()
  if mystr:
    for letter in mystr:
      s.push(letter)
  return ''.join([s.pop() for a in range(s.size())])

print revstring('apple')