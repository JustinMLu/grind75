class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums -> array of integers
        # target -> target summy bummy

        num_dict = {}

        # key: the number | value: the index
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        # now O(n) look for the other number using dict
        for i in range(len(nums)):
            other_num = target - nums[i] # other_num is what we wanna find
            
            # if the target num exists and it's not our current one
            if other_num in num_dict and num_dict[other_num] != i:
                return [i, num_dict[other_num]]