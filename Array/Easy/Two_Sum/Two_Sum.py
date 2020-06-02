# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i in range(len(nums)):
            new_dict[nums[i]]=i
        for i in range(len(nums)):
            result = [i]
            second_number = target - nums[i]
            index = new_dict.get(second_number)
            if index is None:
                pass
            else:
                if result[0] == index:
                    pass
                else:
                    result.append(index)
                    return result