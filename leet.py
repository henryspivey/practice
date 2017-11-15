def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # current = 0
    # next = 1
    # while len(nums) > next :
    #     if nums[current] + nums[next] == target:
    #         return [current, next]        
    #     else:
    #         next += 1
    #         if next == len(nums):
    #             current += 1
    #             next = 0
    #         if next == current:
    #             next +=1   
    # return "No two sum found"
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
            print buff_dict
    
    return None, None


print twoSum([2,7,11,15], 9)
# print twoSum([11,2,15,7], 9)
# print twoSum([2,5,5,11], 10)


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    i = 0
    j = 0
    for x in nums:
        if x != 0:
            nums[i] = x
            i += 1
        else: 
            j += 1
            # counts the zeros
    for z in range(j):
        nums[i+z] = 0
    return nums


print moveZeroes([0,1,0,3,12])