def solve(nums):
    ans = 0

    i = 0
    while i < len(nums):
        check = nums[i] >= 0

        max_ = float("-inf")
        while i < len(nums) and (nums[i] >= 0) == check:
            max_ = max(max_, nums[i])
            i += 1

        ans += max_
    
    print(ans)



for i in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))
    solve(nums)