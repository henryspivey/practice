# Directed graphs adjacency matrix 
# Space Complexity O(v^2)
class DirectedGraphAM:
  def __init__(self, size):
    self.vertices = {}
    self.size = size

  def addEdge(self, u, v, weight):
    if not u in self.vertices:
      self.vertices[u] = {}
    self.vertices[u][v] = weight


  def neighbors(self, u):
    if u in self.vertices:
      for v in self.vertices[u]:
        yield (v, self.vertices[u][v])

  def __repr__(self):
    rep = 'graph:['
    for u in range(self.size):
      if u in self.vertices:
        rep += str(u) + ":"
        for v in self.vertices[u]:
          rep += '(' + str(v) + "," + str(self.vertices[u][v]) + "),"

    return rep + ']'

b = DirectedGraphAM(4)
b.addEdge(0,2,99)
print b
b.addEdge(0, 3, 88)
print b.neighbors(3)


class DirectedGraphAL:
  def __init__(self, size):
    self.size = size
    self.vertices = [None]*size

  def addEdge(self, u, v, weight):
    if self.vertices[u] is None:
        self.vertices[u] = []
    for e in self.vertices[u]:
      if e[0] == v:
        self.vertices[u].remove(e)
    self.vertices[u].append( (v, weight))

  def neighbors(self, u):
    if self.vertices[u]:
      for e in self.vertices[u]:
        yield e

  def __repr__(self):
    rep = 'graph:['
    for u in range(self.size):
      if self.vertices[u]:
        rep += str(u) + ":"
        rep += ','.join(map(str, self.vertices[u]))
        rep += ';'
    return rep + ']'

d = DirectedGraphAL(3)
d.addEdge(0, 1, 99)
print d
d.addEdge(0, 1, 777)
d.addEdge(0, 2, 777)
d.addEdge(1, 2, 77)
print d