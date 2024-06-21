def solve(nums):
    i = 0
    count = 0

    while i < len(nums):
        if nums[i] < 0:
            while i < len(nums) and nums[i] <= 0:
                nums[i] *= -1
                i += 1
        
            count += 1

        i += 1

    print(sum(nums), count)


for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    solve(nums)