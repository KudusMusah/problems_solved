def solve(nums):
    nums.sort()

    l, r = 0, len(nums) - 1
    ans = 0
    while l < r:
        ans += (nums[r] - nums[l])
        l += 1
        r -= 1

    return ans


for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(solve(nums))