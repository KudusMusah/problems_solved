n = int(input())
nums = list(map(int, input().split()))
nums.sort()

l = 0
ans = 0

for r in range(n):
    if nums[r] - nums[l] <= 5:
        ans = max(ans, r-l+1)
    else:
        l += 1

print(ans)