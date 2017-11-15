# A Python program to print all 
# permutations using library function
from itertools import permutations
import operator


# def findMaxPerm(nums):
#   arrangements = list()
#   arrangement = ""
#   if(not len(nums)):
#     return 0
#   else:
#     perms = list(permutations(nums))
#     # print perms
#     # # all permutations are in perm
#     # # # loop through perm, get value of list for each index
#     for perm in perms:
#       arrangements.append(''.join(str(i) for i in perm))
#     return max(arrangements)
  
# print findMaxPerm([3, 30, 34, 5, 9])


def maxSubArray(arr):
  arrangements = list()
  if(not len(arr)):
    return 0;
  else:
    # iterate over array to keep track of length (i) 
    for i in range(1, len(arr)+1):
      currentLength = i
      # generate permutations of sub arrays based on currentLength
      subarray = list(permutations(arr, i));      
      for element in range(len(subarray)):
        currentPerm = subarray[element]
        currentSum = sum(subarray[element]) # gives the sum of a permutation
        arrangements.append({'array': currentPerm, 'sum': currentSum})


    arrangements.sort(key=operator.itemgetter('sum'))
    print arrangements[len(arrangements)-1]

# sumSubArray([-2,1,-3,4,-1,2,1,-5,4])
# sumSubArray([-2,1,-3])
      
