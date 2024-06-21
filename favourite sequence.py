def solve(nums):
    l, r = 0, len(nums) - 1
    output = []

    while l <= r:
        if l == r:
            output.append(nums[l])
            break
        output.extend([nums[l], nums[r]])
        l += 1
        r -= 1
    
    print(*output)


for i in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    solve(nums)