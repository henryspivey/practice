# Hashing involves mapping items to a value and storing them in a table
# % arithmetic is typically used in hashing algorithms since the result must be in the range of slot names
# Folding method
# divide the item into equal pieces, add them together to give the resulting hash value
# Midsquare method
# square the item, extract a portion of the resulting digits

def hash(aString, tablesize):
  sum = 0
  for pos in range(len(aString)):
    sum = sum + ord(aString[pos])

  return sum%tablesize

    