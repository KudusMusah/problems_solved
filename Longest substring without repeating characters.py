from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = defaultdict(int)
        ans, l = 0, 0

        for r in range(len(s)):
            hashmap[s[r]] += 1

            while hashmap[s[r]] > 1:
                hashmap[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans
