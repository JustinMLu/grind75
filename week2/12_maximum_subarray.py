class Solution:
    def maxSubArray(self, nums) -> int:
        
        n = len(nums)
        
        # base case
        if n == 1:
            return nums[0]

        # another base case just to go faster
        if n == 2:
            # both positive? return sum
            if nums[0] > 0 and nums[1] > 0:
                return nums[0] + nums[1]
            
            # only one or more is negative? return max
            else:
                return max(nums[0], nums[1])

        max_sum = nums[0]
        current_sum = 0
        i = 0

        while i < n:
            # add nums[i] to sum
            current_sum += nums[i]

            # cmp with max
            if current_sum > max_sum:
                max_sum = current_sum
        
            # if we go negative we might as well restart at nums+1
            if current_sum < 0:
                # if we're at the end just return
                if i == n-1:
                    return max_sum
                
                # reset and restart
                current_sum = 0
            
            i += 1
                
        return max_sum
        