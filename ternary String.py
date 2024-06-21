from collections import defaultdict

def solve(s):
    hashmap = defaultdict(int)
    ans = float("inf")
    
    l = 0
    for r in range(len(s)):
        hashmap[s[r]] += 1
        
        while len(hashmap) == 3 and l < r:
            ans= min(ans, r-l+1)
            
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
             
    if ans == float("inf"): ans = 0
    print(ans)            


for i in range(int(input())):
    s = input()
    
    solve(s)
