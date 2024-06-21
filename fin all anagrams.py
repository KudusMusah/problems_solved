from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, k = len(s), len(p)

        p_counter = Counter(p)
        curr_counter = Counter(s[:k])

        output = []
        if curr_counter == p_counter:
            output.append(0)
        
        for l in range(N-k):
            r = l + k
            curr_counter[s[l]] -= 1
            curr_counter[s[r]] += 1

            if curr_counter == p_counter:
                output.append(l+1)

        return output
        