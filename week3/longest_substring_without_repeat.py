class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print("NOT my best work but im strapped for time")

        # length
        n = len(s)

        # base case
        if n == 1:
            return 1

        # another one for fun
        elif n == 2:
            if s[0] == s[1]:
                return 1
            return 2
        
        # start iteration
        letter_dict = {} # letter -> idx
        max_size = 0
        cur_size = 0
        i = 0

        while i < n:
            
            # if no repeat, add to dict and increment
            if s[i] not in letter_dict:
                
                # increment cur_size
                cur_size += 1

                # cmp with max
                if cur_size > max_size:

                    max_size = cur_size
                letter_dict[s[i]] = i
                i += 1

            # if we found a repeat, we gotta restart to the right of the orig. repeat
            else:
                # reset size, move i backwards, reset letter_dict
                cur_size = 0
                new_i = letter_dict[s[i]] + 1
                i = new_i
                letter_dict = {}
            
        
        return max_size
