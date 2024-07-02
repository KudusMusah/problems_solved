def solve(s):
    hashmap = {}

    ans = float("Inf")

    for i in range(len(s)):
        hashmap[s[i]] = i

        if len(hashmap) == 3:
            curr_len = max(hashmap.values()) - min(hashmap.values()) + 1
            ans = min(ans, curr_len)

    return ans if ans != float("inf") else 0



for i in range(int(input())):
    s = input()
    
    print(solve(s))
