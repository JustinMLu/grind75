class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cur_min = prices[0]
        max_profit = 0

        for p in prices:
            if p < cur_min: # update new minimum, but we keep going
                cur_min = p
            
            else: # else, p is >= the current min, so p is a potential sell day --> check its profits
                max_profit = max(max_profit, p - cur_min)
        
        return max_profit