class Solution:
    def isPalindrome(self, s: str) -> bool:

        lowered = list(s.lower())
        
        # base case: "" or " " or "aa" or ",," or ".." or "  "
        if len(s) == 0 or len(s) == 1 or (len(s) == 2 and lowered[0] == lowered[1]):
            print("base case triggered")
            return True

        print("base case not triggered - cleaning")
        cleaned = []
        for l in lowered:
            if l.isalpha() or l.isdigit():
                cleaned.append(l)

        
        print("cleaned array: ", cleaned)

        # fucking check AGAIN
        if (len(cleaned) == 1 or len(cleaned) == 0):
            return True

        # use 2ptrs to check everything, return false the second we mismatch
        head = 0
        tail = len(cleaned) - 1

        while (head <= tail):
            if cleaned[head] == cleaned[tail]:
                head = head + 1
                tail = tail - 1
            else:
                return False
        
        return True